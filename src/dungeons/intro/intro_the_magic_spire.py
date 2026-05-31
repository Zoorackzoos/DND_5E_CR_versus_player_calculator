from src.universal_functions.display.print_encounter_difficulty_concisely import print_encounter_difficulty_concisely
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_xp_values import get_encounter_difficulty_from_xp_values
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

path_to_csv_file = "../../../sheets/monsters_all_stats_homebrew.csv"

def get_z_lvl_1_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # 1st z level
    # 4 of these
    manes_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                  string="Demon, Manes",
                                                  path_to_csv_file=path_to_csv_file,
                                                  tab_amount=tab_amount)
    manes_xp = get_xp_from_single_enemy_cr(cr=manes_cr, tab_amount=tab_amount)
    # 9 of these
    calculus_monster_limits_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                    string="Calculus Monster, Limit",
                                                                    path_to_csv_file=path_to_csv_file,
                                                                    tab_amount=tab_amount)
    calculus_monster_limits_xp = get_xp_from_single_enemy_cr(cr=calculus_monster_limits_cr, tab_amount=tab_amount)
    # 2 of these
    withering_gnoll_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                            string="Gnoll Witherling",
                                                            path_to_csv_file=path_to_csv_file,
                                                            tab_amount=tab_amount)
    withering_gnoll_xp = get_xp_from_single_enemy_cr(cr=withering_gnoll_cr, tab_amount=tab_amount)

    z_lvl_1_monster_xps = [manes_xp, manes_xp,
                           calculus_monster_limits_xp, calculus_monster_limits_xp,
                           calculus_monster_limits_xp, calculus_monster_limits_xp,
                           withering_gnoll_xp]
    z_lvl_1_encounter_difficulty = get_encounter_difficulty_from_xp_values(player_levels=player_levels,
                                                                           monster_xp_values=z_lvl_1_monster_xps,
                                                                           tab_amount=tab_amount)
    return z_lvl_1_encounter_difficulty

def get_z_lvl_2_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # 2nd z level
    # 4 of these
    troglodyte_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Troglodyte",
                                                       path_to_csv_file=path_to_csv_file,
                                                       tab_amount=tab_amount)
    troglodyte_xp = get_xp_from_single_enemy_cr(cr=troglodyte_cr, tab_amount=tab_amount)
    # 1 of these
    animated_object_armor_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                  string="Animated Object, Armor",
                                                                  path_to_csv_file=path_to_csv_file,
                                                                  tab_amount=tab_amount)
    animated_object_armor_xp = get_xp_from_single_enemy_cr(cr=animated_object_armor_cr, tab_amount=tab_amount)
    # 3 of these
    lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                   string="Misc. Creature, Lizard",
                                                   path_to_csv_file=path_to_csv_file,
                                                   tab_amount=tab_amount)
    lizard_xp = get_xp_from_single_enemy_cr(cr=lizard_cr, tab_amount=tab_amount)
    # 2 of these
    giant_lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Misc. Creature, Giant Lizard",
                                                         path_to_csv_file=path_to_csv_file,
                                                         tab_amount=tab_amount)
    giant_lizard_xp = get_xp_from_single_enemy_cr(cr=giant_lizard_cr, tab_amount=tab_amount)
    # 3 of these
    tri_flower_frond_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                             string="Tri-Flower Frond",
                                                             path_to_csv_file=path_to_csv_file,
                                                             tab_amount=tab_amount)
    tri_flower_frond_xp = get_xp_from_single_enemy_cr(cr=tri_flower_frond_cr, tab_amount=tab_amount)
    # 3 and then 6
    wolf_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                 string="Misc. Creature, Wolf",
                                                 path_to_csv_file=path_to_csv_file,
                                                 tab_amount=tab_amount)
    wolf_xp = get_xp_from_single_enemy_cr(cr=wolf_cr, tab_amount=tab_amount)
    # 1 of these
    spectator_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                      string="Beholder, Spectator",
                                                      path_to_csv_file=path_to_csv_file,
                                                      tab_amount=tab_amount)
    spectator_xp = get_xp_from_single_enemy_cr(cr=spectator_cr, tab_amount=tab_amount)

    z_lvl_2_monster_xps = [troglodyte_xp, troglodyte_xp,
                           animated_object_armor_xp,
                           lizard_xp, lizard_xp,
                           giant_lizard_xp,
                           tri_flower_frond_xp,
                           wolf_xp, wolf_xp,
                           wolf_xp, wolf_xp
                           #spectator_xp #just make it so this guy asks for ice cream, and the kitchen has ice cream
                           ]
    z_lvl_2_encounter_difficulty = get_encounter_difficulty_from_xp_values(player_levels=player_levels,
                                                                           monster_xp_values=z_lvl_2_monster_xps,
                                                                           tab_amount=tab_amount)
    return z_lvl_2_encounter_difficulty

def get_z_lvl_3_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # z lvl 3
    # 3 of these
    polar_bear_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Misc. Creature, Polar Bear",
                                                       path_to_csv_file=path_to_csv_file,
                                                       tab_amount=tab_amount)
    polar_bear_xp = get_xp_from_single_enemy_cr(cr=polar_bear_cr, tab_amount=tab_amount)
    z_lvl_3_monster_xps = [polar_bear_xp, polar_bear_xp, polar_bear_xp]
    z_lvl_3_encounter_difficulty = get_encounter_difficulty_from_xp_values(player_levels=player_levels,
                                                                           monster_xp_values=z_lvl_3_monster_xps,
                                                                           tab_amount=tab_amount)
    return z_lvl_3_encounter_difficulty

def intro_the_magic_spire(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_spire")
    player_levels = [4,4,4,4]

    z_lvl_1_encounter_difficulty = get_z_lvl_1_encounter_difficulty(player_levels, tab_amount)

    z_lvl_2_encounter_difficulty = get_z_lvl_2_encounter_difficulty(player_levels, tab_amount)

    z_lvl_3_encounter_difficulty = get_z_lvl_3_encounter_difficulty(player_levels, tab_amount)

    print(tab_amount,"calculations complete :-3")
    print_encounter_difficulty_concisely(dict_in_question=z_lvl_1_encounter_difficulty,tab_amount=tab_amount+"\t")
    print_encounter_difficulty_concisely(dict_in_question=z_lvl_2_encounter_difficulty,tab_amount=tab_amount+"\t")
    print_encounter_difficulty_concisely(dict_in_question=z_lvl_3_encounter_difficulty,tab_amount=tab_amount+"\t")

if __name__ == "__main__":
    intro_the_magic_spire()