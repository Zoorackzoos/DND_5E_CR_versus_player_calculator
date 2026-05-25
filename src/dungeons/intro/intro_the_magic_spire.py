from src.universal_functions.craft_cr_from_monster_stat_block import craft_cr_from_monster_stat_block, \
    plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_average_damage import get_average_damage_no_print
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

def get_z_lvl_1_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # 1st z level
    # 4 of these
    manes_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                  string="Demon, Manes",
                                                  tab_amount=tab_amount)
    manes_xp = get_xp_from_single_enemy_cr(cr=manes_cr, tab_amount=tab_amount)
    # 9 of these
    calculus_monster_limits_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                    string="Calculus Monster, Limit",
                                                                    tab_amount=tab_amount)
    calculus_monster_limits_xp = get_xp_from_single_enemy_cr(cr=calculus_monster_limits_cr, tab_amount=tab_amount)
    # 2 of these
    withering_gnoll_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                            string="Gnoll Witherling",
                                                            tab_amount=tab_amount)
    withering_gnoll_xp = get_xp_from_single_enemy_cr(cr=withering_gnoll_cr, tab_amount=tab_amount)

    z_lvl_1_monster_xps = [manes_xp, manes_xp, manes_xp, manes_xp,
                           calculus_monster_limits_xp, calculus_monster_limits_xp,
                           calculus_monster_limits_xp, calculus_monster_limits_xp,
                           calculus_monster_limits_xp, calculus_monster_limits_xp,
                           withering_gnoll_xp, withering_gnoll_xp]
    z_lvl_1_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                            monster_xp_values=z_lvl_1_monster_xps,
                                                            tab_amount=tab_amount)
    return z_lvl_1_encounter_difficulty

def get_z_lvl_2_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # 2nd z level
    # 4 of these
    troglodyte_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Troglodyte",
                                                       tab_amount=tab_amount)
    troglodyte_xp = get_xp_from_single_enemy_cr(cr=troglodyte_cr, tab_amount=tab_amount)
    # 1 of these
    animated_object_armor_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                  string="Animated Object, Armor",
                                                                  tab_amount=tab_amount)
    animated_object_armor_xp = get_xp_from_single_enemy_cr(cr=animated_object_armor_cr, tab_amount=tab_amount)
    # 3 of these
    lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                   string="Misc. Creature, Lizard",
                                                   tab_amount=tab_amount)
    lizard_xp = get_xp_from_single_enemy_cr(cr=lizard_cr, tab_amount=tab_amount)
    # 2 of these
    giant_lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Misc. Creature, Giant Lizard",
                                                         tab_amount=tab_amount)
    giant_lizard_xp = get_xp_from_single_enemy_cr(cr=giant_lizard_cr, tab_amount=tab_amount)
    # 3 of these
    tri_flower_frond_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                             string="Tri-Flower Frond",
                                                             tab_amount=tab_amount)
    tri_flower_frond_xp = get_xp_from_single_enemy_cr(cr=tri_flower_frond_cr, tab_amount=tab_amount)
    # 3 and then 6
    wolf_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                 string="Misc. Creature, Wolf",
                                                 tab_amount=tab_amount)
    wolf_xp = get_xp_from_single_enemy_cr(cr=wolf_cr, tab_amount=tab_amount)
    # 1 of these
    spectator_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                      string="Beholder, Spectator",
                                                      tab_amount=tab_amount)
    spectator_xp = get_xp_from_single_enemy_cr(cr=spectator_cr, tab_amount=tab_amount)

    z_lvl_2_monster_xps = [troglodyte_xp, troglodyte_xp, troglodyte_xp, troglodyte_xp,
                           animated_object_armor_xp,
                           lizard_xp, lizard_xp, lizard_xp,
                           giant_lizard_xp, giant_lizard_xp,
                           tri_flower_frond_xp, tri_flower_frond_xp,
                           wolf_xp, wolf_xp, wolf_xp,
                           wolf_xp, wolf_xp, wolf_xp, wolf_xp, wolf_xp, wolf_xp,
                           spectator_xp]
    z_lvl_2_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                            monster_xp_values=z_lvl_2_monster_xps,
                                                            tab_amount=tab_amount)
    return z_lvl_2_encounter_difficulty

def get_z_lvl_3_encounter_difficulty(player_levels: list[int], tab_amount: str) -> dict[
    str, int | float | dict[str, int] | str]:
    # z lvl 3
    # 3 of these
    polar_bear_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Misc. Creature, Polar Bear",
                                                       tab_amount=tab_amount)
    polar_bear_xp = get_xp_from_single_enemy_cr(cr=polar_bear_cr, tab_amount=tab_amount)
    z_lvl_3_monster_xps = [polar_bear_xp, polar_bear_xp, polar_bear_xp]
    z_lvl_3_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                            monster_xp_values=z_lvl_3_monster_xps,
                                                            tab_amount=tab_amount)
    return z_lvl_3_encounter_difficulty

def intro_the_magic_spire(tab_amount="\t"):
    #TODO: change dungeon to be not as hard as it is right now

    #i did the CR calculations for the Limit calculus monster at some point but i deleted it some time ago
    #regardless i want to be able to do it again flexibly
    #so...
    #TODO: add a column to the spreadsheet that has all of the craft cr function's necessities so the code can call it here

    print(tab_amount,"intro_the_magic_spire")
    player_levels = [4,4,4,4]

    z_lvl_1_encounter_difficulty = get_z_lvl_1_encounter_difficulty(player_levels, tab_amount)

    z_lvl_2_encounter_difficulty = get_z_lvl_2_encounter_difficulty(player_levels, tab_amount)

    z_lvl_3_encounter_difficulty = get_z_lvl_3_encounter_difficulty(player_levels, tab_amount)

    print(tab_amount,"calculations complete :-3")
    print_dictionary_nicely(dict_in_question=z_lvl_1_encounter_difficulty,tab_amount=tab_amount)
    print_dictionary_nicely(dict_in_question=z_lvl_2_encounter_difficulty,tab_amount=tab_amount)
    print_dictionary_nicely(dict_in_question=z_lvl_3_encounter_difficulty,tab_amount=tab_amount)


if __name__ == "__main__":
    intro_the_magic_spire()