def get_value_from_encounter_or_monster_dict(
        encounter_or_monster_dict,
        header,
        HEADER_ALIASES):
    """
    

    :param encounter_or_monster_dict:
    :param header:
    :param HEADER_ALIASES:
    :return:
    """
    possible_keys = [header]
    possible_keys += HEADER_ALIASES.get(header, [])
    possible_keys += [header.lower()]

    for key in possible_keys:
        if key in encounter_or_monster_dict:
            value = encounter_or_monster_dict[key]

            if value is None:
                return ""

            return value

    return ""

def get_normalized_encounter_or_monster_name(encounter_or_monster_name):
    """
    strip(). makes the text less noise.
    lower(). to standardize it.

    :param encounter_or_monster_name:
    :return:
    """
    return str(encounter_or_monster_name).strip().lower()
