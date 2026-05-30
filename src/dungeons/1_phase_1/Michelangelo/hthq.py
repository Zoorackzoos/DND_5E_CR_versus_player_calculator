from src.universal_functions.craft_cr_from_monster_stat_block import craft_cr_from_monster_stat_block, \
    plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_average_damage import get_average_damage
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

def get_tokka_cr(tab_amount="\t"):
    print(tab_amount,"get_tokka_cr")
    tab_amount += "\t"

    #rush bash is greater
    damage_dice_dict_rush_bash = \
        {
            6: 4,
            "constant": 4
        }
    """
    damage_dice_dict_physic_ray = \
        {
            12: 2,
            "constant": 2
        }
    """

    #print(tab_amount,"4d6 + 4 = ",get_average_damage(dice_dict=damage_dice_dict_rush_bash,tab_amount=tab_amount))
    #print(tab_amount,"2d12 + 2 = ",get_average_damage(dice_dict=damage_dice_dict_physic_ray,tab_amount=tab_amount))
    craft_cr_from_monster_stat_block(hit_points=50,
                                     armor_class=14,
                                     average_damage=get_average_damage(dice_dict=damage_dice_dict_rush_bash,tab_amount=tab_amount),
                                     attack_modifier=3,
                                     has_legendary_action=False,
                                     has_flight=False,
                                     resistance_count=0,
                                     immunity_count=0,
                                     weakness_count=0,
                                     save_dc=12,
                                     is_spellcaster=False,
                                     regeneration_per_round=0,
                                     multiattack_count=0,
                                     ability_count=0,
                                     recharge_damage=0,
                                     tab_amount=tab_amount)

def get_rahzar_cr(tab_amount="\t"):
    print(tab_amount,"get_rahzar_cr")
    tab_amount += "\t"
    rahzar_dice_dict = \
        {
            6 : 4,
            "constant": 4
        }
    rahzar_monster_dict = \
        {
            "hp": 50,
            "ac": 13,
            "average_damage": get_average_damage(dice_dict=rahzar_dice_dict,tab_amount=tab_amount),
            "attack_modifier": 3,
            "has_legendary_action": False,
            "has_flight": False,
            "resistance_count": 0,
            "immunity_count": 0,
            "weakness_count": 0,
            "save_dc": 12,
            "is_spellcaster": False,
            "regeneration_per_round": 0,
            "multiattack_count": 0,
            "ability_count": 0,
            "recharge_damage": 0,
            "limited_use_damage": 0,
            "bonus_action_damage": 0,
            "legendary_action_damage": 0,
            "ability_cr_weight": 0,
            "str_modifier": 2,
            "dex_modifier": 2,
            "con_modifier": 0,
            "int_modifier": -3,
            "wis_modifier": -1,
            "cha_modifier": -2
        }
    plug_monster_var_values_into_get_cr_from_monster(monster_var=rahzar_monster_dict,tab_amount=tab_amount)

def get_cyborg_cr(tab_amount="\t"):
    cyborg_dice_dict = \
        {
            8: 1,
            "constant": 2
        }
    cyborg_monster_dict = \
        {
            "hp": 15,
            "ac": 11,
            "average_damage": get_average_damage(dice_dict=cyborg_dice_dict, tab_amount=tab_amount),
            "attack_modifier": 3,
            "has_legendary_action": False,
            "has_flight": False,
            "resistance_count": 0,
            "immunity_count": 0,
            "weakness_count": 0,
            "save_dc": 0,
            "is_spellcaster": False,
            "regeneration_per_round": 0,
            "multiattack_count": 0,
            "ability_count": 0,
            "recharge_damage": 0,
            "limited_use_damage": 0,
            "bonus_action_damage": 0,
            "legendary_action_damage": 0,
            "ability_cr_weight": 0,
            "str_modifier": 2,
            "dex_modifier": 2,
            "con_modifier": 0,
            "int_modifier": 0,
            "wis_modifier": 0,
            "cha_modifier": -1
        }
    plug_monster_var_values_into_get_cr_from_monster(monster_var=cyborg_monster_dict, tab_amount=tab_amount)

#murder all human traffickers. every single one.
def hthq(tab_amount="\t"):
    print(tab_amount,"hthq")

    player_levels = [4,4,4,4]

    hthq_path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew.csv"

    purple_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Purple Foot Clan Ninja",
                                                         path_to_csv_file=hthq_path_to_csv_file,
                                                         tab_amount=tab_amount)
    purple_ninja_xp = get_xp_from_single_enemy_cr(cr=purple_ninja_cr,
                                                  tab_amount=tab_amount)

    pink_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Pink Foot Clan Ninja",
                                                       path_to_csv_file=hthq_path_to_csv_file,
                                                       tab_amount=tab_amount)
    pink_ninja_xp = get_xp_from_single_enemy_cr(cr=pink_ninja_cr,
                                                tab_amount=tab_amount)

    tokka_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                  string="Tokka the evil blue turtle",
                                                  path_to_csv_file=hthq_path_to_csv_file,
                                                  tab_amount=tab_amount)
    tokka_xp = get_xp_from_single_enemy_cr(cr=tokka_cr,
                                           tab_amount=tab_amount)

    rahzar_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                   string="Rahzar the evil puppy monster",
                                                   path_to_csv_file=hthq_path_to_csv_file,
                                                   tab_amount=tab_amount)
    rahzar_xp = get_xp_from_single_enemy_cr(cr=rahzar_cr,
                                            tab_amount=tab_amount)

    lvl_1_monsters_xps = [purple_ninja_xp, purple_ninja_xp, purple_ninja_xp,
                      purple_ninja_xp, purple_ninja_xp, purple_ninja_xp,
                      pink_ninja_xp,
                          tokka_xp,rahzar_xp]

    lvl_1_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                          monster_xp_values=lvl_1_monsters_xps,
                                                          tab_amount=tab_amount)

    blue_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Blue Foot Clan Ninja",
                                                       path_to_csv_file=hthq_path_to_csv_file,
                                                       tab_amount=tab_amount)
    blue_ninja_xp = get_xp_from_single_enemy_cr(cr=blue_ninja_cr,
                                                tab_amount=tab_amount)

    green_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                        string="Green Foot Clan Ninja",
                                                        path_to_csv_file=hthq_path_to_csv_file,
                                                        tab_amount=tab_amount)
    green_ninja_xp = get_xp_from_single_enemy_cr(cr=green_ninja_cr,
                                                 tab_amount=tab_amount)

    yellow_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Yellow Foot Clan Ninja",
                                                         path_to_csv_file=hthq_path_to_csv_file,
                                                         tab_amount=tab_amount)
    yellow_ninja_xp = get_xp_from_single_enemy_cr(cr=yellow_ninja_cr,
                                                  tab_amount=tab_amount)

    white_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                        string="White Foot Clan Ninja",
                                                        path_to_csv_file=hthq_path_to_csv_file,
                                                        tab_amount=tab_amount)
    white_ninja_xp = get_xp_from_single_enemy_cr(cr=white_ninja_cr,
                                                 tab_amount=tab_amount)

    exposed_evil_ninja_cyborg_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                                      string="exposed evil ninja cyborg",
                                                                      path_to_csv_file=hthq_path_to_csv_file,
                                                                      tab_amount=tab_amount)
    exposed_evil_ninja_cyborg_xp = get_xp_from_single_enemy_cr(cr=exposed_evil_ninja_cyborg_cr,
                                                               tab_amount=tab_amount)

    lvl_2_monsters_xps = \
        [
            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, blue_ninja_xp, # airlock
            green_ninja_xp, green_ninja_xp, green_ninja_xp, green_ninja_xp, #showers
            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, yellow_ninja_xp, #chamber
            white_ninja_xp, white_ninja_xp, blue_ninja_xp, blue_ninja_xp, #computer room

            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp,
            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, #computer mainframe
            exposed_evil_ninja_cyborg_xp, exposed_evil_ninja_cyborg_xp,
            exposed_evil_ninja_cyborg_xp, exposed_evil_ninja_cyborg_xp,
            exposed_evil_ninja_cyborg_xp, exposed_evil_ninja_cyborg_xp #computer mainframe
        ]

    lvl_2_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                          monster_xp_values=lvl_2_monsters_xps,
                                                          tab_amount=tab_amount)

    print(tab_amount,"calculations complete :-3")
    print_dictionary_nicely(dict_in_question=lvl_1_encounter_difficulty,
                            tab_amount=tab_amount)
    print_dictionary_nicely(dict_in_question=lvl_2_encounter_difficulty,
                            tab_amount=tab_amount)



if __name__ == "__main__":
    tab_amount="\t"
    hthq(tab_amount=tab_amount)
    #get_tokka_cr(tab_amount=tab_amount)
    #get_rahzar_cr(tab_amount=tab_amount)
    #get_cyborg_cr(tab_amount=tab_amount)