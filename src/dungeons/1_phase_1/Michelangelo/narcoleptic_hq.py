from src.universal_functions.craft_cr_from_monster_stat_block import plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_average_damage import get_average_damage
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from src.universal_functions.vars import spreadsheet_enums
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


def get_mauser_cr(tab_amount="\t"):
    print(tab_amount,"get_mauser_cr")
    tab_amount += "\t"
    mauser_dice_dict = \
        {
            4: 1,
            "constant": 2
        }
    mauser_monster_dict = \
        {
            "hp": 10,
            "ac": 11,
            "average_damage": get_average_damage(dice_dict=mauser_dice_dict, tab_amount=tab_amount),
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
            "str_modifier": 3,
            "dex_modifier": 0,
            "con_modifier": 0,
            "int_modifier": 0,
            "wis_modifier": 0,
            "cha_modifier": 0
        }
    return plug_monster_var_values_into_get_cr_from_monster(monster_var=mauser_monster_dict,tab_amount=tab_amount)

def narcoleptic_hq(tab_amount="\t"):
    print(tab_amount,"narcoleptic_hq")
    tab_amount += "\t"

    path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

    player_levels = [4,4,4,4]

    """
    1 pink ninja
    2 orange ninjas
    2 white ninjas
    """
    pink_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Pink Foot Clan Ninja",
                                                       path_to_csv_file=path_to_csv_file,
                                                       tab_amount=tab_amount)
    orange_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Orange Foot Clan Ninja",
                                                         path_to_csv_file=path_to_csv_file,
                                                         tab_amount=tab_amount)
    white_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                        string="White Foot Clan Ninja",
                                                        path_to_csv_file=path_to_csv_file,
                                                        tab_amount=tab_amount)
    lvl_1_monster_cr_values = \
    [
        pink_ninja_cr,
        orange_ninja_cr, orange_ninja_cr,
        white_ninja_cr, white_ninja_cr,
    ]
    lvl_1_difficulty = get_encounter_difficulty_from_cr_values( player_levels=player_levels,
                                                                monster_cr_values=lvl_1_monster_cr_values,
                                                                tab_amount=tab_amount)

    """
    1 yellow ninja
    3 green ninjas
    6 mausers
    """
    yellow_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Yellow Foot Clan Ninja",
                                                         path_to_csv_file=path_to_csv_file,
                                                         tab_amount=tab_amount)
    green_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                        string="Green Foot Clan Ninja",
                                                        path_to_csv_file=path_to_csv_file,
                                                        tab_amount=tab_amount)
    mauser_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                   string="mauser",
                                                   path_to_csv_file=path_to_csv_file,
                                                   tab_amount=tab_amount)

    lvl_2_monster_cr_values = \
        [
            yellow_ninja_cr,
            green_ninja_cr, green_ninja_cr, green_ninja_cr,
            mauser_cr, mauser_cr, mauser_cr,
            mauser_cr, mauser_cr, mauser_cr
        ]
    lvl_2_difficulty = get_encounter_difficulty_from_cr_values(player_levels=player_levels,
                                                               monster_cr_values=lvl_2_monster_cr_values,
                                                               tab_amount=tab_amount)

    bebop_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                  string="Bebop",
                                                  path_to_csv_file=path_to_csv_file,
                                                  tab_amount=tab_amount)
    rocksteady_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                       string="Rocksteady",
                                                       path_to_csv_file=path_to_csv_file,
                                                       tab_amount=tab_amount)

    lvl_3_monster_cr_values = \
        [
            bebop_cr, rocksteady_cr
        ]
    lvl_3_difficulty = get_encounter_difficulty_from_cr_values( player_levels=player_levels,
                                                                monster_cr_values=lvl_3_monster_cr_values,
                                                                tab_amount=tab_amount)

    print(tab_amount,"calculations complete :-3")
    print(tab_amount,"lvl_1_difficulty")
    print_dictionary_nicely(dict_in_question=lvl_1_difficulty,tab_amount=tab_amount+"\t")
    print(tab_amount, "lvl_2_difficulty")
    print_dictionary_nicely(dict_in_question=lvl_2_difficulty, tab_amount=tab_amount + "\t")
    print(tab_amount, "lvl_3_difficulty")
    print_dictionary_nicely(dict_in_question=lvl_3_difficulty, tab_amount=tab_amount + "\t")

if __name__ == "__main__":
    tab_amount = "\t"
    narcoleptic_hq(tab_amount=tab_amount)
    #get_mauser_cr(tab_amount=tab_amount)