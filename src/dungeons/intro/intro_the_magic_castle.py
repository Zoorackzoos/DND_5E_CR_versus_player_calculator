from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_CR_from_monster import plug_monster_var_values_into_get_CR_from_monster
from src.universal_functions.get_XP_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_damage_per_round import get_damage_per_round_no_print
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.stats.convert_monster_modifiers_to_stats import convert_monster_modifiers_to_stats
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict

#TODO: create Enums for the spreadsheet headers so i can call them instead of string literals
#TODO: design the get_rows_from_dict_onparam_type_and_string to be more smoother. currently if you do a precise search it gives a list with one dict which is awkdward.
#TODO: make the searching of the database more applicable on this program in general. it's more conveint to cntl+F on the spreadsheet on google sheets

def get_skeleton_cr(tab_amount="\t"):
    print(tab_amount,"get_skeleton_cr")
    skeleton_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict, param_type="Name", string="Skeleton", tab_amount=tab_amount)[0]
    print(tab_amount,"skeleton_row:")
    print(tab_amount+"\t",skeleton_row)
    skeleton_cr = float(skeleton_row["CR"])
    print(tab_amount,"skeleton_cr :",skeleton_cr)
    return skeleton_cr

def get_skeleton_war_horse_cr(tab_amount="\t"):
    print(tab_amount,"get_skeleton_war_horse_cr")
    skeleton_war_horse_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,param_type="Name",string="Skeleton, Warhorse",tab_amount=tab_amount)[0]
    print(tab_amount,"skeleton_war_horse_row:")
    print(tab_amount+"\t",skeleton_war_horse_row)
    #TODO: fix the columns here. when i pull this, it's pulled as a string which is annoying asf.
    skeleton_war_horse_cr = float(skeleton_war_horse_row["CR"])
    print(tab_amount,"skeleton_war_horse_cr :",skeleton_war_horse_cr)
    return skeleton_war_horse_cr

def get_skeleton_minotaur_cr(tab_amount="\t"):
    #TODO: refactor this function into a universal
    print(tab_amount,"get_skeleton_minotaur_cr")
    skeleton_minotaur_row = \
    get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict, param_type="Name",
                                                string="Skeleton, Minotaur", tab_amount=tab_amount)[0]
    print(tab_amount, "skeleton_minotaur_row:")
    print(tab_amount + "\t", skeleton_minotaur_row)
    skeleton_minotaur_cr = float(skeleton_minotaur_row["CR"])
    print(tab_amount, "skeleton_minotaur_cr :", skeleton_minotaur_cr)
    return skeleton_minotaur_cr

def get_cr_from_monster(param_type,string,tab_amount="\t"):
    print(tab_amount,"get_cr_from_monster")
    tab_amount += "\t"

    monster_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict, param_type=param_type,string=string,tab_amount=tab_amount)[0]
    print(tab_amount,"monster_row:")
    print(tab_amount+"\t",monster_row)
    monster_cr = float(monster_row["CR"])
    print(tab_amount,"monster_cr :",monster_cr)
    return monster_cr

def intro_the_magic_castle(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_castle")
    tab_amount += "\t"

    player_levels = [3,3,3,3]

    skeleton_cr = get_skeleton_cr(tab_amount=tab_amount)
    skeleton_war_horse_cr = get_skeleton_war_horse_cr(tab_amount=tab_amount)
    skeleton_xp = get_xp_from_single_enemy_cr(CR=skeleton_cr, tab_amount=tab_amount)
    skeleton_war_horse_xp = get_xp_from_single_enemy_cr(CR=skeleton_war_horse_cr, tab_amount=tab_amount)
    inner_castle_enemies = [skeleton_xp,skeleton_xp,skeleton_xp,skeleton_war_horse_xp,skeleton_war_horse_xp,skeleton_xp]
    inner_castle_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=inner_castle_enemies,tab_amount=tab_amount)

    skeleton_minotaur_cr = get_skeleton_minotaur_cr(tab_amount=tab_amount)
    skeleton_minotaur_xp = get_xp_from_single_enemy_cr(CR=skeleton_minotaur_cr,tab_amount=tab_amount)
    tower_of_power_enemies = [skeleton_minotaur_xp]
    tower_of_power_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=tower_of_power_enemies,tab_amount=tab_amount)

    giant_skeleton_cr = get_cr_from_monster(param_type="Name",string="Skeleton, Giant",tab_amount=tab_amount)
    giant_skeleton_xp = get_xp_from_single_enemy_cr(CR=giant_skeleton_cr, tab_amount=tab_amount)
    tower_of_faith_enemies = [giant_skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,skeleton_xp,]
    tower_of_faith_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=tower_of_faith_enemies,tab_amount=tab_amount)

    print(tab_amount,"calculations complete :-3")

    print(tab_amount,"inner_castle_difficulty")
    print_dictionary_nicely(dict_in_question=inner_castle_difficulty, tab_amount=tab_amount+"\t")
    print(tab_amount,"tower_of_power_difficulty")
    print_dictionary_nicely(dict_in_question=tower_of_power_difficulty, tab_amount=tab_amount+"\t")
    print(tab_amount,"tower_of_faith_difficulty")
    print_dictionary_nicely(dict_in_question=tower_of_faith_difficulty,tab_amount=tab_amount+"\t")

if __name__ == "__main__":
    intro_the_magic_castle()