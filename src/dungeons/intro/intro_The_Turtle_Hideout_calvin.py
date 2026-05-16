from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_array_header import print_array_header_and_array_piece
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_XP_from_single_enemy_CR import get_XP_from_single_enemy_CR
from src.universal_functions.get_damage_per_round import get_damage_per_round
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.spreadsheet_stuff.get_row_from_array_based_on_search_string import get_row_from_array_based_on_search_string
from src.universal_functions.spreadsheet_stuff.get_row_from_dict_on_param_type_and_string import \
    get_row_from_dict_on_param_type_and_string
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict
from src.universal_functions.get_CR_from_monster import get_CR_from_monster, \
    plug_monster_var_values_into_get_CR_from_monster


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

def get_hoopmaster_CR(tab_amount="\t"):
    print(tab_amount, "get_hoopmaster_CR")
    tab_amount += "\t"

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
            "inl": 0,
            "wis": 0,
            "cha": 0,
            "attack_bonus": 3,
            "has_legendary_action": False,
            "has_flight": False,
            "resistance_count": 0,
            "immunity_count": 0,
            "save_dc": 0,
            "is_spellcaster": False,
            "regeneration_per_second": 0,
            "multiattack_count": 0,
            "ability_count": 1,
            "average_damage": get_damage_per_round(dice_dict=hoopmaster_dice_dict, tab_amount=tab_amount + "\t")
        }
    hoopmaster_cr = plug_monster_var_values_into_get_CR_from_monster(monster_var=hoopmaster_stockman_stat_block,
                                                                     tab_amount=tab_amount + "\t")
    print(tab_amount, "hoopmaster_cr = ", hoopmaster_cr)
    return hoopmaster_cr

def get_baxster_CR(tab_amount="\t"):
    print(tab_amount, "get_baxster_CR")
    tab_amount += "\t"

    baxster_dice_dict = \
        {
            4: 5
        }
    baxster_stockman_stat_block = \
        {
            "hp": 90,
            "ac": 11,
            "speed, flight": 60,
            "speed, ground": 30,
            "str": 0,
            "dex": 0,
            "con": 3,
            "inl": 3,
            "wis": 0,
            "cha": -3,
            "attack_bonus": 5,
            "has_legendary_action": False,
            "has_flight": True,
            "resistance_count": 0,
            "immunity_count": 0,
            "save_dc": 13,
            "is_spellcaster": False,
            "regeneration_per_second": 0,
            "multiattack_count": 0,
            "ability_count": 0,
            "average_damage": get_damage_per_round(dice_dict=baxster_dice_dict, tab_amount=tab_amount + "\t")
        }
    baxster_cr = plug_monster_var_values_into_get_CR_from_monster(monster_var=baxster_stockman_stat_block,
                                                                  tab_amount=tab_amount + "\t")
    return baxster_cr

def intro_the_Turtle_Hideout_calvin(tab_amount="\t"):
    print(tab_amount,"intro_the_Turtle_Hideout_calvin")
    tab_amount += "\t"

    player_levels = [3,3,3,3]

    hoopmaster_CR = get_hoopmaster_CR(tab_amount=tab_amount)
    baxster_CR = get_baxster_CR(tab_amount=tab_amount)

    bandit_dict = get_row_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,param_type="Name",string="NPC, Bandit",tab_amount=tab_amount)[0]
    bandit_cr = bandit_dict["CR"]

    bandit_xp = get_XP_from_single_enemy_CR(CR=bandit_cr,tab_amount=tab_amount)
    hoopmaster_xp = get_XP_from_single_enemy_CR(CR=hoopmaster_CR,tab_amount=tab_amount)
    baxster_xp = get_XP_from_single_enemy_CR(CR=baxster_CR,tab_amount=tab_amount)

    monster_xp_list_lvl_1 = [bandit_xp,bandit_xp,bandit_xp,bandit_xp]
    monster_xp_list_lvl_2 = [bandit_xp,hoopmaster_xp,bandit_xp]
    monster_xp_list_lvl_3 = [bandit_xp,bandit_xp,baxster_xp,bandit_xp,bandit_xp]

    lvl_1_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=monster_xp_list_lvl_1,tab_amount=tab_amount)
    lvl_2_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=monster_xp_list_lvl_2,tab_amount=tab_amount)
    lvl_3_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=monster_xp_list_lvl_3,tab_amount=tab_amount)

    print()
    print(tab_amount,"calculations finalized!")
    print()

    print_dictionary_nicely(dict=lvl_1_encounter_difficulty,tab_amount=tab_amount)
    print_dictionary_nicely(dict=lvl_2_encounter_difficulty,tab_amount=tab_amount)
    print_dictionary_nicely(dict=lvl_3_encounter_difficulty,tab_amount=tab_amount)

if __name__ == "__main__":
    tab_amount = "\t"
    #search_database(tab_amount=tab_amount)
    intro_the_Turtle_Hideout_calvin(tab_amount=tab_amount)
