import re
from pathlib import Path

from src.universal_functions.vars import spreadsheet_enums


KNOWN_TOP_LEVEL_SECTIONS = [
    "metadata",
    "core stats",
    "ability scores",
    "saving throws",
    "skills",
    "wri",
    "senses",
    "languages",
    "cr inputs",
    "actions",
]


SPREADSHEET_KEY_ENUMS = {
    "name": "NAME",
    "size": "SIZE",
    "type": "TYPE",
    "cr": "CR",
    "url": "URL",
    "font": "FONT",
    "author": "AUTHOR",
    "hp": "HP",
    "ac": "AC",
    "speed": "SPEEDS",
    "alignment": "ALIGN",
    "str_numeric_stat": "STR",
    "dex_numeric_stat": "DEX",
    "con_numeric_stat": "CON",
    "int_numeric_stat": "INT",
    "wis_numeric_stat": "WIS",
    "cha_numeric_stat": "CHA",
    "saving_throws": "SAVING_THROWS",
    "skills": "SKILLS",
    "wri": "WEAKNESSES_RESISTANCES_AND_IMMUNITIES",
    "senses": "SENSES",
    "languages": "LANGUAGES",
    "additional": "ADDITIONAL",
    "average_damage": "AVERAGE_DAMAGE",
    "attack_modifier": "ATTACK_MODIFIER",
    "has_legendary_action": "HAS_LEGENDARY_ACTION",
    "legendary_action_damage": "LEGENDARY_ACTION_DAMAGE",
    "has_flight": "HAS_FLIGHT",
    "resistance_count": "RESISTANCE_COUNT",
    "immunity_count": "IMMUNITY_COUNT",
    "weakness_count": "WEAKNESS_COUNT",
    "save_dc": "SAVE_DC",
    "is_spellcaster": "IS_SPELLCASTER",
    "regeneration_per_round": "REGENERATION_PER_ROUND",
    "multiattack_count": "MULTIATTACK_COUNT",
    "ability_count": "ABILITY_COUNT",
    "ability_cr_weight": "ABILITY_CR_WEIGHT",
    "recharge_damage": "RECHARGE_DAMAGE",
    "limited_use_damage": "LIMITED_USE_DAMAGE",
    "bonus_action_damage": "BONUS_ACTION_DAMAGE",
}


def normalize_key(value):
    return clean_markdown_text(value).strip().lower().replace(" ", "_")


def normalize_lookup(value):
    return str(value).strip().lower().replace("_", " ")


def clean_markdown_text(value):
    value = str(value).strip()
    value = value.replace("\\_", "_")
    value = value.replace("\\+", "+")
    value = value.replace("\\#", "#")
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\2", value)
    value = value.rstrip("  ")
    return value


def clean_action_name(value):
    value = str(value).strip()
    value = value.replace("\\_", "_")
    value = value.replace("\\+", "+")
    value = value.replace("\\#", "#")
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", value)
    value = re.sub(r"^action\s*-\s*", "", value, flags=re.IGNORECASE)
    return value.strip()


def parse_scalar(value):
    value = clean_markdown_text(value)

    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in ["none", ""]:
        return value

    if re.fullmatch(r"[-+]?\d+", value):
        return int(value)
    if re.fullmatch(r"[-+]?\d+\.\d+", value):
        return float(value)

    return value


def split_comma_list(value):
    value = clean_markdown_text(value)
    return [item.strip() for item in value.split(",") if item.strip() != ""]


def parse_key_value_line(line):
    if ":" not in line:
        return None, None

    key, value = line.split(":", 1)
    return normalize_key(key), parse_scalar(value)


def get_enum_expression(enum_class, enum_class_name, raw_value):
    normalized_raw_value = normalize_lookup(raw_value)

    for enum_value in enum_class:
        if normalize_lookup(enum_value.value) == normalized_raw_value:
            return "spreadsheet_enums." + enum_class_name + "." + enum_value.name + ".value"

    return repr(raw_value)


def get_wri_enum_expression(damage_type, defense_kind):
    normalized_damage_type = normalize_lookup(damage_type).replace(" ", "_").upper()
    normalized_defense_kind = normalize_lookup(defense_kind)

    if normalized_defense_kind in ["resistant", "resistance", "resistances"]:
        suffix = "RESISTANT"
    elif normalized_defense_kind in ["immune", "immunity", "immunities"]:
        suffix = "IMMUNE"
    else:
        suffix = "WEAKNESS"

    enum_name = normalized_damage_type + "_" + suffix

    if hasattr(spreadsheet_enums.WRIEnums, enum_name):
        return "spreadsheet_enums.WRIEnums." + enum_name + ".value"

    return repr(str(damage_type) + suffix.lower())


def get_list_expression(value_expressions):
    if len(value_expressions) == 0:
        return "''"
    if len(value_expressions) == 1:
        return value_expressions[0]

    return '", ".join([' + ", ".join(value_expressions) + "])"


def slugify_python_name(value):
    value = clean_markdown_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = value.strip("_")

    if value == "":
        return "monster"
    if value[0].isdigit():
        value = "monster_" + value

    return value


def parse_markdown_stat_block(path_to_markdown_file, tab_amount="\t"):
    print(tab_amount, "parse_markdown_stat_block")
    tab_amount += "\t"

    path_to_markdown_file = Path(path_to_markdown_file)
    print(tab_amount, "path_to_markdown_file =", path_to_markdown_file)

    if not path_to_markdown_file.exists():
        print(tab_amount, "ERROR: parse_markdown_stat_block: markdown stat block file does not exist.")
        exit()

    parsed_stat_block = {
        "metadata": {},
        "core_stats": {},
        "ability_scores": {},
        "saving_throws": {},
        "skills": {},
        "wri": {
            "weak": [],
            "resistant": [],
            "immune": [],
        },
        "senses": {},
        "languages": [],
        "cr_inputs": {},
        "actions": [],
        "ignored_sections": [],
    }

    current_section = None
    current_action = None

    with open(path_to_markdown_file, encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if line == "":
                continue

            heading_match = re.match(r"^(#+)\s+(.+)$", line)

            if heading_match:
                heading_level = len(heading_match.group(1))
                raw_heading_text = heading_match.group(2)
                heading_text = clean_markdown_text(raw_heading_text)
                normalized_heading = normalize_lookup(heading_text)

                if heading_level == 1:
                    if normalized_heading in KNOWN_TOP_LEVEL_SECTIONS:
                        current_section = normalized_heading.replace(" ", "_")
                    else:
                        current_section = "ignored"
                        parsed_stat_block["ignored_sections"].append(heading_text)
                    current_action = None
                elif current_section == "actions" and heading_level == 2:
                    current_action = {
                        "name": clean_action_name(raw_heading_text),
                    }
                    parsed_stat_block["actions"].append(current_action)
                elif normalized_heading == "cr inputs":
                    current_section = "cr_inputs"
                    current_action = None

                continue

            if current_section == "ignored" or current_section is None:
                continue

            if current_section == "languages" and line.startswith("-"):
                parsed_stat_block["languages"].append(
                    clean_markdown_text(line[1:])
                )
                continue

            key, value = parse_key_value_line(line)

            if key is None:
                continue

            if current_section == "metadata":
                parsed_stat_block["metadata"][key] = value
            elif current_section == "core_stats":
                parsed_stat_block["core_stats"][key] = value
            elif current_section == "ability_scores":
                parsed_stat_block["ability_scores"][key] = value
            elif current_section == "saving_throws":
                parsed_stat_block["saving_throws"][key] = value
            elif current_section == "skills":
                parsed_stat_block["skills"][key] = value
            elif current_section == "wri":
                if key in ["weak", "weakness", "weaknesses"]:
                    parsed_stat_block["wri"]["weak"] += split_comma_list(value)
                elif key in ["resistant", "resistance", "resistances"]:
                    parsed_stat_block["wri"]["resistant"] += split_comma_list(value)
                elif key in ["immune", "immunity", "immunities"]:
                    parsed_stat_block["wri"]["immune"] += split_comma_list(value)
            elif current_section == "senses":
                parsed_stat_block["senses"][key] = value
            elif current_section == "cr_inputs":
                parsed_stat_block["cr_inputs"][key] = value
            elif current_section == "actions" and current_action is not None:
                current_action[key] = value

    return parsed_stat_block


def get_defaulted_monster_properties(parsed_stat_block, tab_amount="\t"):
    print(tab_amount, "get_defaulted_monster_properties")
    tab_amount += "\t"

    metadata = parsed_stat_block["metadata"]
    core_stats = parsed_stat_block["core_stats"]
    ability_scores = parsed_stat_block["ability_scores"]
    senses = parsed_stat_block["senses"]
    cr_inputs = parsed_stat_block["cr_inputs"]

    if len(parsed_stat_block["languages"]) == 0:
        print(tab_amount, "languages header missing or empty. Defaulting to Common.")
        languages = ["common"]
    else:
        languages = parsed_stat_block["languages"]

    if (len(parsed_stat_block["wri"]["weak"]) == 0 and
            len(parsed_stat_block["wri"]["resistant"]) == 0 and
            len(parsed_stat_block["wri"]["immune"]) == 0):
        print(tab_amount, "WRI missing or empty. Defaulting to None.")

    monster_properties = {
        "name": metadata.get("name", "Unnamed Monster"),
        "size": core_stats.get("size", "medium"),
        "type": core_stats.get("type", "monstrosity"),
        "cr": metadata.get("cr", "????"),
        "url": metadata.get("url", ""),
        "font": metadata.get("font", ""),
        "author": metadata.get("author", ""),
        "hp": core_stats.get("hp", 1),
        "ac": core_stats.get("ac", 10),
        "speed": core_stats.get("speed", 30),
        "alignment": core_stats.get("alignment", "U"),
        "str_numeric_stat": ability_scores.get("str_numeric_stat", 10),
        "dex_numeric_stat": ability_scores.get("dex_numeric_stat", 10),
        "con_numeric_stat": ability_scores.get("con_numeric_stat", 10),
        "int_numeric_stat": ability_scores.get("int_numeric_stat", 10),
        "wis_numeric_stat": ability_scores.get("wis_numeric_stat", 10),
        "cha_numeric_stat": ability_scores.get("cha_numeric_stat", 10),
        "saving_throws": parsed_stat_block["saving_throws"],
        "skills": parsed_stat_block["skills"],
        "wri": parsed_stat_block["wri"],
        "senses": senses.get("senses", "Normal"),
        "languages": languages,
        "additional": metadata.get("additional", "None"),
        "actions": parsed_stat_block["actions"],
    }

    for key, default_value in {
        "average_damage": 0,
        "attack_modifier": 0,
        "has_legendary_action": False,
        "legendary_action_damage": 0,
        "has_flight": False,
        "resistance_count": len(parsed_stat_block["wri"]["resistant"]),
        "immunity_count": len(parsed_stat_block["wri"]["immune"]),
        "weakness_count": len(parsed_stat_block["wri"]["weak"]),
        "save_dc": 0,
        "is_spellcaster": False,
        "regeneration_per_round": 0,
        "multiattack_count": 0,
        "ability_count": 0,
        "ability_cr_weight": 2,
        "recharge_damage": 0,
        "limited_use_damage": 0,
        "bonus_action_damage": 0,
    }.items():
        monster_properties[key] = cr_inputs.get(key, default_value)

    return monster_properties


def get_saving_throw_expression(saving_throws):
    if len(saving_throws) == 0:
        return "spreadsheet_enums.SavingThrowsEnums.NONE.value"

    value_expressions = []

    for key in saving_throws:
        enum_name = key.upper()

        if hasattr(spreadsheet_enums.SavingThrowsEnums, enum_name):
            value_expressions.append(
                "spreadsheet_enums.SavingThrowsEnums." + enum_name + ".value"
            )

    return get_list_expression(value_expressions)


def get_skills_expression(skills):
    if len(skills) == 0:
        return "spreadsheet_enums.SkillsEnums.NONE.value"

    value_expressions = []

    for key in skills:
        enum_name = key.upper()

        if hasattr(spreadsheet_enums.SkillsEnums, enum_name):
            value_expressions.append(
                "spreadsheet_enums.SkillsEnums." + enum_name + ".value"
            )
        else:
            value_expressions.append(repr(str(key).title()))

    return get_list_expression(value_expressions)


def get_wri_expression(wri):
    value_expressions = []

    for damage_type in wri["weak"]:
        value_expressions.append(get_wri_enum_expression(damage_type, "weak"))
    for damage_type in wri["resistant"]:
        value_expressions.append(get_wri_enum_expression(damage_type, "resistant"))
    for damage_type in wri["immune"]:
        value_expressions.append(get_wri_enum_expression(damage_type, "immune"))

    if len(value_expressions) == 0:
        return "spreadsheet_enums.WRIEnums.NONE.value"

    return get_list_expression(value_expressions)


def get_languages_expression(languages):
    value_expressions = []

    for language in languages:
        value_expressions.append(
            get_enum_expression(
                enum_class=spreadsheet_enums.LanguagesEnums,
                enum_class_name="LanguagesEnums",
                raw_value=language
            )
        )

    return get_list_expression(value_expressions)


def get_monster_value_expression(key, value):
    if key == "size":
        return get_enum_expression(spreadsheet_enums.SizeEnums, "SizeEnums", value)
    if key == "type":
        return get_enum_expression(spreadsheet_enums.CreatureTypesEnums, "CreatureTypesEnums", value)
    if key == "cr":
        return repr(value)
    if key == "font":
        return get_enum_expression(spreadsheet_enums.FontTypesEnums, "FontTypesEnums", value)
    if key == "author":
        return get_enum_expression(spreadsheet_enums.AuthorFontTypesEnums, "AuthorFontTypesEnums", value)
    if key == "alignment":
        return get_enum_expression(spreadsheet_enums.AlignmentEnums, "AlignmentEnums", value)
    if key == "saving_throws":
        return get_saving_throw_expression(value)
    if key == "skills":
        return get_skills_expression(value)
    if key == "wri":
        return get_wri_expression(value)
    if key == "senses":
        return get_enum_expression(spreadsheet_enums.SensesEnums, "SensesEnums", value)
    if key == "languages":
        return get_languages_expression(value)

    return repr(value)


def build_python_dictionary_file_text(monster_properties, dict_variable_name=None):
    if dict_variable_name is None:
        dict_variable_name = slugify_python_name(monster_properties["name"]) + "_monster_dict"

    ordered_keys = [
        "name",
        "size",
        "type",
        "cr",
        "url",
        "font",
        "author",
        "hp",
        "ac",
        "speed",
        "alignment",
        "str_numeric_stat",
        "dex_numeric_stat",
        "con_numeric_stat",
        "int_numeric_stat",
        "wis_numeric_stat",
        "cha_numeric_stat",
        "saving_throws",
        "skills",
        "wri",
        "senses",
        "languages",
        "additional",
        "average_damage",
        "attack_modifier",
        "has_legendary_action",
        "legendary_action_damage",
        "has_flight",
        "resistance_count",
        "immunity_count",
        "weakness_count",
        "save_dc",
        "is_spellcaster",
        "regeneration_per_round",
        "multiattack_count",
        "ability_count",
        "ability_cr_weight",
        "recharge_damage",
        "limited_use_damage",
        "bonus_action_damage",
    ]

    lines = [
        "from src.universal_functions.vars import spreadsheet_enums",
        "",
        "",
        dict_variable_name + " = \\",
        "    {",
    ]

    for key in ordered_keys:
        spreadsheet_enum_name = SPREADSHEET_KEY_ENUMS[key]
        key_expression = (
            "spreadsheet_enums.SpreadsheetKeysEnums."
            + spreadsheet_enum_name
            + ".value"
        )
        value_expression = get_monster_value_expression(key, monster_properties[key])

        lines.append("        " + key_expression + " :")
        lines.append("            " + value_expression + ",")

    lines.append('        "actions" :')
    lines.append("            " + repr(monster_properties["actions"]) + ",")
    lines.append("    }")
    lines.append("")

    return "\n".join(lines)


def interpret_markdown_stat_block_into_python_file(
        path_to_markdown_file,
        path_to_python_file,
        dict_variable_name=None,
        tab_amount="\t"
):
    print(tab_amount, "interpret_markdown_stat_block_into_python_file")
    tab_amount += "\t"

    parsed_stat_block = parse_markdown_stat_block(
        path_to_markdown_file=path_to_markdown_file,
        tab_amount=tab_amount
    )
    monster_properties = get_defaulted_monster_properties(
        parsed_stat_block=parsed_stat_block,
        tab_amount=tab_amount
    )
    python_file_text = build_python_dictionary_file_text(
        monster_properties=monster_properties,
        dict_variable_name=dict_variable_name
    )

    path_to_python_file = Path(path_to_python_file)
    path_to_python_file.parent.mkdir(parents=True, exist_ok=True)

    with open(path_to_python_file, "w", encoding="utf-8") as file:
        file.write(python_file_text)

    print(tab_amount, "path_to_python_file =", path_to_python_file)
    print(tab_amount, "python stat block dictionary file created")

    return monster_properties


if __name__ == "__main__":
    """
    interpret_markdown_stat_block_into_python_file(
        path_to_markdown_file="temp_monster_directory/Template Monster, Parser Trial.md",
        path_to_python_file="temp_monster_directory/Template Monster, Parser Trial.py"
    )
    """
    phase_1_foot_clan_ninja_path_list = \
    [
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 blue foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 blue foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 green foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 green foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 orange foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 orange foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 pink foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 pink foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 purple foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 purple foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 white foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 white foot clan ninja.py"
        ],
        [
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 yellow foot clan ninja.md",
            "../../dungeons/1_phase_1/Michelangelo/monster_related/monster_dict_files/phase_1_foot_clan_ninjas/phase 1 yellow foot clan ninja.py"
        ],
    ]

    for path in phase_1_foot_clan_ninja_path_list:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=path[0],
            path_to_python_file=path[1]
        )