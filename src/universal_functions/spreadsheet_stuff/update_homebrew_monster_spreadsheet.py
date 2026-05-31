import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_HOMEBREW_MONSTER_SPREADSHEET = (
    PROJECT_ROOT / "sheets" / "monsters_all_stats_homebrew.csv"
)


HEADER_ALIASES = {
    "Name": ["name"],
    "Size": ["size"],
    "Type": ["type"],
    "CR": ["cr"],
    "URL": ["url"],
    "Font": ["font", "source"],
    "Author": ["author"],
    "HP": ["hp", "hit_points"],
    "AC": ["ac", "armor_class"],
    "Speeds": ["speeds", "speed"],
    "Align.": ["align", "alignment"],
    "STR": ["str", "strength"],
    "DEX": ["dex", "dexterity"],
    "CON": ["con", "constitution"],
    "INT": ["int", "intelligence"],
    "WIS": ["wis", "wisdom"],
    "CHA": ["cha", "charisma"],
    "Sav. Throws": ["sav_throws", "saving_throws"],
    "Skills": ["skills"],
    "WRI": ["wri"],
    "Senses": ["senses"],
    "Languages": ["languages"],
    "Additional": ["additional"],
}


def get_value_from_monster_dict(monster_dict, header):
    possible_keys = [header]
    possible_keys += HEADER_ALIASES.get(header, [])
    possible_keys += [header.lower()]

    for key in possible_keys:
        if key in monster_dict:
            value = monster_dict[key]

            if value is None:
                return ""

            return value

    return ""


def get_normalized_monster_name(monster_name):
    return str(monster_name).strip().lower()


def get_row_from_monster_dict(monster_dict, fieldnames):
    row = {}

    for fieldname in fieldnames:
        row[fieldname] = get_value_from_monster_dict(
            monster_dict=monster_dict,
            header=fieldname
        )

    return row


def get_duplicate_index(rows, monster_name):
    normalized_monster_name = get_normalized_monster_name(monster_name)

    for index, row in enumerate(rows):
        if get_normalized_monster_name(row.get("Name", "")) == normalized_monster_name:
            return index

    return None


def update_homebrew_monster_spreadsheet(
        monster_dict,
        path_to_csv_file=DEFAULT_HOMEBREW_MONSTER_SPREADSHEET,
        duplicate_action="ask",
        tab_amount="\t"
):
    print(tab_amount, "update_homebrew_monster_spreadsheet")
    tab_amount += "\t"

    path_to_csv_file = Path(path_to_csv_file)
    print(tab_amount, "path_to_csv_file =", path_to_csv_file)

    if not path_to_csv_file.exists():
        print(tab_amount, "ERROR: homebrew monster spreadsheet does not exist.")
        exit()

    monster_name = get_value_from_monster_dict(
        monster_dict=monster_dict,
        header="Name"
    )

    if str(monster_name).strip() == "":
        print(tab_amount, "ERROR: monster_dict must include a Name or name value.")
        exit()

    with open(path_to_csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if fieldnames is None:
        print(tab_amount, "ERROR: spreadsheet must have a header row.")
        exit()

    new_row = get_row_from_monster_dict(
        monster_dict=monster_dict,
        fieldnames=fieldnames
    )

    duplicate_index = get_duplicate_index(
        rows=rows,
        monster_name=monster_name
    )

    if duplicate_index is not None:
        print(tab_amount, "duplicate monster found =", monster_name)

        if duplicate_action == "ask":
            answer = input(
                "A monster named "
                + str(monster_name)
                + " already exists. Overwrite it? y/n: "
            )

            if answer.strip().lower() in ["y", "yes"]:
                duplicate_action = "overwrite"
            else:
                duplicate_action = "stop"

        if duplicate_action == "overwrite":
            print(tab_amount, "overwriting existing monster row")
            rows[duplicate_index] = new_row
        elif duplicate_action == "stop":
            print(tab_amount, "stopping without changing the spreadsheet")
            exit()
        else:
            print(tab_amount, "ERROR: duplicate_action must be ask, overwrite, or stop.")
            exit()
    else:
        print(tab_amount, "adding new monster =", monster_name)
        rows.append(new_row)

    with open(path_to_csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(tab_amount, "spreadsheet updated")
    return new_row


if __name__ == "__main__":
    example_monster = {
        "Name": "Example Monster",
        "Size": "Medium",
        "Type": "Monstrosity",
        "CR": 1,
        "HP": 30,
        "AC": 13,
        "average_damage": 9,
        "attack_modifier": 3,
    }

    update_homebrew_monster_spreadsheet(
        monster_dict=example_monster
    )
