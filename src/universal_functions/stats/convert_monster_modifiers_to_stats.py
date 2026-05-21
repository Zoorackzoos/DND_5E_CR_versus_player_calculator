from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.stats.get_numeric_stat_from_modifier import get_numeric_stat_from_modifier


def convert_monster_modifiers_to_stats(monster_dict,tab_amount="\t"):
    """
    hoopmaster_dice_dict = \
        {
            6: 2,
            "constant": 2
        }
    hoopmaster_stockman_stat_block = \
        {
            "hp": 30,
            "ac": 13,
            "speed, ground": 30,
            "str": 1,
            "dex": 1,
            "con": 1,
            "int": 0,
            "wis": 0,
            "cha": 0,
            "attack_bonus": 3,
            "has_legendary_action": False,
            "has_flight": False,
            "resistance_count": 0,
            "immunity_count": 0,
            "save_dc": 0,
            "is_spellcaster": False,
            "regeneration_per_round": 0,
            "multiattack_count": 0,
            "ability_count": 1,
            "average_damage": get_damage_per_round(dice_dict=hoopmaster_dice_dict, tab_amount=tab_amount + "\t")
        }

    :param monster_dict:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"convert_monster_modifiers_to_stats")
    tab_amount += "\t"
    new_monster_dict = monster_dict.copy()

    new_monster_dict["str_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["str_modifier"])
    new_monster_dict["dex_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["dex_modifier"])
    new_monster_dict["con_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["con_modifier"])
    new_monster_dict["int_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["int_modifier"])
    new_monster_dict["wis_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["wis_modifier"])
    new_monster_dict["cha_modifier"] = get_numeric_stat_from_modifier(modifier=monster_dict["cha_modifier"])
    return new_monster_dict

if __name__ == "__main__":
     monster_dict = \
         {
             "str_modifier": 2,
             "dex_modifier": 2,
             "con_modifier": 3,
             "int_modifier": 0,
             "wis_modifier": 0,
             "cha_modifier": 0
         }
     monster_dict_2 = convert_monster_modifiers_to_stats(monster_dict=monster_dict)
     print_dictionary_nicely(dict_in_question=monster_dict_2)