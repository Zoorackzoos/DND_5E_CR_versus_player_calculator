from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.craft_cr_from_monster_stat_block import plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_damage_per_round import get_damage_per_round_no_print
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.stats.convert_monster_modifiers_to_stats import convert_monster_modifiers_to_stats
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict


def search_database(search_database_tab_amount="\t"):
    all_humanoids = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,
                                                                param_type="Type", string="humanoid",
                                                                get_rows_tab_amount=search_database_tab_amount)

    """
    how to sort lists of dicts
        don't ask bruh
    the key contains the key it sorts by
    reverse is if you want top to bottom or bottom to top
    """
    all_humanoids.sort(
        key=lambda row: float(row["CR"]),
    )

    print_2d_list(list_in_question=all_humanoids, tab_amount=search_database_tab_amount)

"""
i'm going to put stats in as modifiers here.
the stat converter functions will be used to be put into the spreadsheet as i make duncan characters
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
        "average_damage": get_damage_per_round_no_print(dice_dict=hoopmaster_dice_dict)
    }

def get_hoopmaster_cr(get_hoopmaster_cr_tab_amount="\t"):
    print(get_hoopmaster_cr_tab_amount, "get_hoopmaster_CR")
    get_hoopmaster_cr_tab_amount += "\t"

    hoopmaster_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=hoopmaster_stockman_stat_block,
                                                                     tab_amount=get_hoopmaster_cr_tab_amount + "\t")
    print(get_hoopmaster_cr_tab_amount, "hoopmaster_cr = ", hoopmaster_cr)
    return hoopmaster_cr

baxster_dice_dict = \
    {
        4: 3
    }
baxster_stockman_stat_block = \
    {
        "hp": 60,
        "ac": 11,
        "speed, flight": 60,
        "speed, ground": 30,
        "str": 0,
        "dex": 0,
        "con": 3,
        "int": 3,
        "wis": 0,
        "cha": -3,
        "attack_bonus": 5,
        "has_legendary_action": False,
        "has_flight": True,
        "resistance_count": 0,
        "immunity_count": 0,
        "save_dc": 13,
        "is_spellcaster": False,
        "regeneration_per_round": 0,
        "multiattack_count": 0,
        "ability_count": 0,
        "average_damage": get_damage_per_round_no_print(dice_dict=baxster_dice_dict)
    }

def get_baxster_cr(get_baxster_cr_tab_amount="\t"):
    print(get_baxster_cr_tab_amount, "get_baxster_CR")
    get_baxster_cr_tab_amount += "\t"

    baxster_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=baxster_stockman_stat_block,
                                                                  tab_amount=get_baxster_cr_tab_amount + "\t")
    return baxster_cr

def intro_the_turtle_hideout_calvin(intro_the_turtle_hideout_calvin_tab_amount="\t"):
    print(intro_the_turtle_hideout_calvin_tab_amount, "intro_the_Turtle_Hideout_calvin")
    intro_the_turtle_hideout_calvin_tab_amount += "\t"

    player_levels = [3,3,3,3]

    hoopmaster_cr = get_hoopmaster_cr(get_hoopmaster_cr_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    baxster_cr = get_baxster_cr(get_baxster_cr_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)

    bandit_dict = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict, param_type="Name", string="NPC, Bandit", get_rows_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)[0]
    bandit_cr = float(bandit_dict["CR"])

    bandit_xp = get_xp_from_single_enemy_cr(cr=bandit_cr, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    hoopmaster_xp = get_xp_from_single_enemy_cr(cr=hoopmaster_cr, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    baxster_xp = get_xp_from_single_enemy_cr(cr=baxster_cr, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)

    monster_xp_list_lvl_1 = [bandit_xp,bandit_xp,bandit_xp,bandit_xp,bandit_xp,bandit_xp,bandit_xp]
    monster_xp_list_lvl_2 = [bandit_xp,hoopmaster_xp,bandit_xp,bandit_xp,bandit_xp]
    monster_xp_list_lvl_3 = [bandit_xp,bandit_xp,baxster_xp,bandit_xp,bandit_xp]

    lvl_1_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels, monster_xp_values=monster_xp_list_lvl_1, get_encounter_difficulty_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    lvl_2_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels, monster_xp_values=monster_xp_list_lvl_2, get_encounter_difficulty_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    lvl_3_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels, monster_xp_values=monster_xp_list_lvl_3, get_encounter_difficulty_tab_amount=intro_the_turtle_hideout_calvin_tab_amount)

    print()
    print(intro_the_turtle_hideout_calvin_tab_amount, "calculations finalized!")
    print()

    #TODO: give better GUI interface to show each level's title, "lvl #", their enemies's title, individual CR & individual XP
    print_dictionary_nicely(dict_in_question=lvl_1_encounter_difficulty, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    print_dictionary_nicely(dict_in_question=lvl_2_encounter_difficulty, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)
    print_dictionary_nicely(dict_in_question=lvl_3_encounter_difficulty, tab_amount=intro_the_turtle_hideout_calvin_tab_amount)

def convert_hoopmaster_and_baxster_to_numeric_stats(convert_numeric_stats_tab_amount="\t"):
    print(convert_numeric_stats_tab_amount, "convert_hoopmaster_and_baxster_to_numeric_stats")
    convert_numeric_stats_tab_amount += "\t"
    print(convert_numeric_stats_tab_amount, "hoopmaster")
    print_dictionary_nicely(convert_monster_modifiers_to_stats(monster_dict=hoopmaster_stockman_stat_block, tab_amount=convert_numeric_stats_tab_amount + "\t"), tab_amount=convert_numeric_stats_tab_amount + "\t")
    print(convert_numeric_stats_tab_amount, "baxster")
    print_dictionary_nicely(convert_monster_modifiers_to_stats(monster_dict=baxster_stockman_stat_block, tab_amount=convert_numeric_stats_tab_amount + "\t"), tab_amount=convert_numeric_stats_tab_amount + "\t")

if __name__ == "__main__":
    tab_amount = "\t"
    #search_database(tab_amount=tab_amount)
    #intro_the_Turtle_Hideout_calvin(tab_amount=tab_amount)
    convert_hoopmaster_and_baxster_to_numeric_stats(convert_numeric_stats_tab_amount=tab_amount)
