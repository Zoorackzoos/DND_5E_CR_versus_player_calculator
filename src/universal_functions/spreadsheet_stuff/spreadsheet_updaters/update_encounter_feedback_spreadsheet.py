import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ENCOUNTER_FEEDBACK_SPREADSHEET = (
    PROJECT_ROOT / "sheets" / "encounter_feedback.csv"
)


HEADER_ALIASES = {
    "encounter_name": ["name", "encounter"],
    "party_level": ["level"],
    "party_size": ["player_count", "players"],
    "predicted_difficulty": ["predicted"],
    "actual_difficulty": ["actual"],
    "monster_count": ["monsters"],
    "total_monster_xp": ["total_xp"],
    "adjusted_xp": ["adjusted_monster_xp"],
    "rounds": ["round_count"],
    "lasted_too_long": ["too_long"],
    "players_downed": ["downed"],
    "players_killed": ["killed", "deaths"],
    "major_resource_drain": ["resource_drain"],
    "terrain_helped_players": ["player_terrain_help"],
    "terrain_helped_monsters": ["monster_terrain_help"],
    "player_synergy_tags": ["synergy_tags"],
    "monster_weakness_tags": ["weakness_tags"],
    "party_thresholds": ["thresholds"],
}


def get_value_from_encounter_dict(encounter_dict, header):
    possible_keys = [header]
    possible_keys += HEADER_ALIASES.get(header, [])
    possible_keys += [header.lower()]

    for key in possible_keys:
        if key in encounter_dict:
            value = encounter_dict[key]

            if value is None:
                return ""

            return value

    return ""


def get_normalized_encounter_name(encounter_name):
    return str(encounter_name).strip().lower()


def get_row_from_encounter_dict(encounter_dict, fieldnames):
    row = {}

    for fieldname in fieldnames:
        row[fieldname] = get_value_from_encounter_dict(
            encounter_dict=encounter_dict,
            header=fieldname
        )

    return row


def get_duplicate_index(rows, encounter_name):
    normalized_encounter_name = get_normalized_encounter_name(encounter_name)

    for index, row in enumerate(rows):
        if get_normalized_encounter_name(row.get("encounter_name", "")) == normalized_encounter_name:
            return index

    return None


def update_encounter_feedback_spreadsheet(
        encounter_dict,
        path_to_csv_file=DEFAULT_ENCOUNTER_FEEDBACK_SPREADSHEET,
        duplicate_action="ask",
        tab_amount="\t"
):
    print(tab_amount, "update_encounter_feedback_spreadsheet")
    tab_amount += "\t"

    path_to_csv_file = Path(path_to_csv_file)
    print(tab_amount, "path_to_csv_file =", path_to_csv_file)

    if not path_to_csv_file.exists():
        print(tab_amount, "ERROR: update_encounter_feedback_spreadsheet: encounter feedback spreadsheet does not exist.")
        exit()

    encounter_name = get_value_from_encounter_dict(
        encounter_dict=encounter_dict,
        header="encounter_name"
    )

    if str(encounter_name).strip() == "":
        print(tab_amount, "ERROR: encounter_dict must include an encounter_name or name value.")
        exit()

    with open(path_to_csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if fieldnames is None:
        print(tab_amount, "ERROR: update_encounter_feedback_spreadsheet: spreadsheet must have a header row.")
        exit()

    new_row = get_row_from_encounter_dict(
        encounter_dict=encounter_dict,
        fieldnames=fieldnames
    )

    duplicate_index = get_duplicate_index(
        rows=rows,
        encounter_name=encounter_name
    )

    if duplicate_index is not None:
        print(tab_amount, "duplicate encounter found =", encounter_name)

        if duplicate_action == "ask":
            answer = input(
                "An encounter named "
                + str(encounter_name)
                + " already exists. Overwrite it? y/n: "
            )

            if answer.strip().lower() in ["y", "yes"]:
                duplicate_action = "overwrite"
            else:
                duplicate_action = "stop"

        if duplicate_action == "overwrite":
            print(tab_amount, "overwriting existing encounter row")
            rows[duplicate_index] = new_row
        elif duplicate_action == "stop":
            print(tab_amount, "stopping without changing the spreadsheet")
            exit()
        else:
            print(tab_amount, "ERROR: duplicate_action must be ask, overwrite, or stop.")
            exit()
    else:
        print(tab_amount, "adding new encounter =", encounter_name)
        rows.append(new_row)

    with open(path_to_csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(tab_amount, "spreadsheet updated")
    return new_row


if __name__ == "__main__":
    example_encounter = {
        "encounter_name": "example_encounter",
        "party_level": 4,
        "party_size": 4,
        "predicted_difficulty": "medium",
        "actual_difficulty": "easy",
        "notes": "Example row.",
    }

    update_encounter_feedback_spreadsheet(
        encounter_dict=example_encounter
    )
