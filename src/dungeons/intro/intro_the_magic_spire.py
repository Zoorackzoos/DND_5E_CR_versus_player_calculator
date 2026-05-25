from src.universal_functions.craft_cr_from_monster_stat_block import craft_cr_from_monster_stat_block, \
    plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_average_damage import get_average_damage_no_print
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


def intro_the_magic_spire(tab_amount="\t"):
    #TODO: finishing getting CR calculations for the magic spire

    print(tab_amount,"intro_the_magic_spire")
    player_levels = [4,4,4,4]

    #1st z level
    #4 of these
    manes_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                  string="Demon, Manes",
                                                  tab_amount=tab_amount)
    #9 of these
    calculus_monster_limits_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                    string="Calculus Monster, Limit",
                                                                    tab_amount=tab_amount)
    #2 of these
    withering_gnoll_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                            string="Gnoll Witherling",
                                                            tab_amount=tab_amount)

    #2nd z level
    #4 of these
    troglodyte_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Troglodyte",
                                                       tab_amount=tab_amount)
    #1 of these
    animated_object_armor_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                  string="Animated Object, Armor",
                                                                  tab_amount=tab_amount)
    #3 of these
    lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                   string="Misc. Creature, Lizard",
                                                   tab_amount=tab_amount)
    #2 of these
    giant_lizard_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Misc. Creature, Giant Lizard",
                                                         tab_amount=tab_amount)
    #3 of these
    tri_flower_frond_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                             string="Tri-Flower Frond",
                                                             tab_amount=tab_amount)
    #3 and then 6
    wolf_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                 string="Misc. Creature, Wolf",
                                                 tab_amount=tab_amount)
    #1 of these
    spectator_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                      string="Beholder, Spectator",
                                                      tab_amount=tab_amount)
    #z lvl 3
    polar_bear_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Misc. Creature, Polar Bear",
                                                       tab_amount=tab_amount)

if __name__ == "__main__":
    intro_the_magic_spire()