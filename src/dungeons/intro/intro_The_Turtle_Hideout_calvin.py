from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_array_header import print_array_header_and_array_piece
from src.universal_functions.spreadsheet_stuff.get_row_from_array_based_on_search_string import get_row_from_array_based_on_search_string
from src.universal_functions.spreadsheet_stuff.get_row_from_dict_on_param_type_and_string import \
    get_row_from_dict_on_param_type_and_string
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict

def search_database(tab_amount="\t"):
    all_humanoids = get_row_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,
                                                               param_type="Type", string="humanoid",
                                                               tab_amount=tab_amount)

    """
    how to sort lists of dicts
        don't ask bruh
    the key contains the key it sorts by
    reverse is if you want top to bottum or bottum to top
    """
    all_humanoids.sort(
        key=lambda row: float(row["CR"]),
    )

    print_2d_list(list_in_question=all_humanoids, tab_amount=tab_amount)

def intro_the_Turtle_Hideout_calvin(tab_amount="\t"):
    print(tab_amount,"intro_the_Turtle_Hideout_calvin")
    tab_amount += "\t"

    player_levels = [3,3,3,3]
    baxster_stockman_stat_block = \
    {
        "hp" : 80,
        "ac" : 11,
        "speed, flight" : 60,
        "speed, ground" : 30,
        "str" : 0,
        "dex" : 0,
        "con" : 3,
        "inl" : 3,
        "wis" : 0,
        "cha" : -3,
        "attack_bonus" : 5,
        "has_legendary_action" : False,
        "resistance_count" : 0,
        "immunity_count": 0,
        "save_dc": 13,
        "is_spellcaster": False,
        "regeneration_per_second": 0,
        "multiattack_count":0,
        "ability_count":0,
    }
    """
    def get_cr_from_monster(
        hit_points,
        armor_class,
        damage_per_round,
        attack_bonus,
        has_legendary_action,
        has_flight,
        resistance_count,
        immunity_count,
        save_dc,
        is_spellcaster,
        regeneration_per_round,
        multiattack_count,
        ability_count,
        tab_amount="\t"
    ):
    
    print(average_damage("2d6"))
    # 7.0

    print(average_damage("2d4 + 1d8"))
    # 9.5
    
    """


if __name__ == "__main__":
    tab_amount = "\t"
    #search_database(tab_amount=tab_amount)
    intro_the_Turtle_Hideout_calvin(tab_amount=tab_amount)
