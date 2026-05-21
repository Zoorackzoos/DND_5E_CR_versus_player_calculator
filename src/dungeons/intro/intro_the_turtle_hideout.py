from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.craft_cr_from_monster_stat_block import plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_average_damage import get_average_damage_no_print, get_average_damage
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.stats.convert_monster_modifiers_to_stats import convert_monster_modifiers_to_stats
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

def get_purple_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_purple_ninja_cr")
    """
    return craft_cr_from_monster_stat_block(
        hit_points=monster_var["hp"],
        armor_class=monster_var["ac"],
        damage_per_round=monster_var["average_damage"],
        attack_modifier=monster_var.get("attack_modifier", 0),
        has_legendary_action=monster_var.get("has_legendary_action", False),
        has_flight=monster_var.get("has_flight", False),
        resistance_count=monster_var.get("resistance_count", 0),
        immunity_count=monster_var.get("immunity_count", 0),
        weakness_count=monster_var.get("weakness_count", 0),
        save_dc=monster_var.get("save_dc", 0),
        is_spellcaster=monster_var.get("is_spellcaster", False),
        regeneration_per_round=monster_var.get("regeneration_per_round", 0),
        multiattack_count=monster_var.get("multiattack_count", 0),
        ability_count=monster_var.get("ability_count", 0),
        recharge_damage=monster_var.get("recharge_damage", 0),
        limited_use_damage=monster_var.get("limited_use_damage", 0),
        bonus_action_damage=monster_var.get("bonus_action_damage", 0),
        legendary_action_damage=monster_var.get("legendary_action_damage", 0),
        ability_cr_weight=monster_var.get("ability_cr_weight", 2),
        tab_amount=tab_amount
    )
    """
    #either attack
    purple_ninja_dice_dict = \
        {
            6 : 1,
            "constant" : 2
        }
    purple_ninja_dictionary = \
        {
            "hp" : 20,
            "ac" : 12,
            "average_damage" : get_average_damage(dice_dict=purple_ninja_dice_dict),
            "attack_modifier" : 3,
            "has_legendary_action" : False,
            "has_flight" : False,
            "resistance_count" : 0,
            "immunity_count" : 0,
            "weakness_count" : 0,
            "save_dc" : 0,
            "is_spellcaster" : False,
            "regeneration_per_round" : 0,
            "multiattack_count" : 0,
            "ability_count" : 0,
            "recharge_damage" : 0,
            "limited_use_damage" : 0,
            "bonus_action_damage" : 0,
            "legendary_action_damage" : 0,
            "ability_cr_weight" : 0,
            "str_modifier" : 0,
            "dex_modifier" : 1,
            "con_modifier" : 1,
            "int_modifier" : 0,
            "wis_modifier" : 0,
            "cha_modifier" : 0
        }
    return plug_monster_var_values_into_get_cr_from_monster(monster_var=purple_ninja_dictionary,tab_amount=tab_amount)

def get_blue_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_blue_ninja_cr")
    blue_ninja_dice_dict = \
        {
            6 : 3,
            "constant" : 3
        }
    blue_ninja_dictionary = \
        {
            "hp" : 20,
            "ac" : 12,
            "average_damage" : get_average_damage_no_print(dice_dict=blue_ninja_dice_dict),
            "attack_modifier" : 5,
            "has_legendary_action" : False,
            "has_flight" : False,
            "multiattack" : 1,
            "str_modifier": 1,
            "dex_modifier": 1,
            "con_modifier": 1,
            "int_modifier": 0,
            "wis_modifier": 0,
            "cha_modifier": 0
        }
    blue_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=blue_ninja_dictionary,tab_amount=tab_amount)
    return blue_ninja_cr

def get_pink_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_pink_ninja_cr")
    pink_ninja_dice_dict = \
        {
            8 : 1,
            "constant" : 2
        }
    pink_ninja_dict = \
        {
            "hp" : 50,
            "ac" : 12,
            "average_damage" : get_average_damage(dice_dict=pink_ninja_dice_dict,tab_amount=tab_amount),
            "attack_modifier" : 3,
            "multiattack_count" : 2
        }
    pink_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=pink_ninja_dict,tab_amount=tab_amount)
    return pink_ninja_cr

def get_orange_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_orange_ninja_cr")
    orange_ninja_dice_dict = \
        {
            12 : 1,
            "constant" : 4
        }
    orange_ninja_dictionary = \
        {
            "hp" : 20,
            "ac" : 15,
            "average_damage" : get_average_damage_no_print(dice_dict=orange_ninja_dice_dict),
            "attack_modifier" : 4,
            "has_legendary_action" : False,
            "has_flight" : False,
            "resistance_count" : 0,
            "immunity_count" : 0,
            "weakness_count" : 0,
            "save_dc" : 0,
            "is_spellcaster" : False,
            "regeneration_per_round" : 0,
            "multiattack_count" : 0,
            "ability_count" : 1,
            "recharge_damage" : 0,
            "limited_use_damage" : 0,
            "legendary_action_damage" : 0,
            "ability_cr_weight" : 1
        }
    orange_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=orange_ninja_dictionary,tab_amount=tab_amount)
    return orange_ninja_cr

def get_white_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_white_ninja_cr")
    white_ninja_dice_dict = \
        {
            12 : 1,
            "constant" : 4
        }
    white_ninja_dictionary = \
        {
            "ac" : 12,
            "hp" : 25,
            "speed, ground" : 30, #not standardized
            "str_numeric" : 14,
            "dex_numeric" : 14,
            "con_numeric" : 12,
            "int_numeric" : 10,
            "wis_numeric" : 10,
            "cha_numeric" : 10,
            "average_damage" : get_average_damage_no_print(dice_dict=white_ninja_dice_dict),
            "ability_count" : 1,
            "ability_cr_weight" : 2,
            "attack_modifier" : 3
        }
    white_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=white_ninja_dictionary,tab_amount=tab_amount)
    return white_ninja_cr

def get_yellow_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_yellow_ninja_cr")
    yellow_ninja_dice_dict = \
        {
            8 : 1,
            "constant" : 4
        }
    yellow_ninja_bomb_damage = \
        {
            6 : 4,
            "constant" : 4
        }
    yellow_ninja_dictionary = \
        {
            "ac" : 12,
            "hp" : 20,
            "speed, ground" : 30,
            "str_numeric" : 12,
            "dex_numeric" : 12,
            "con_numeric" : 12,
            "int_numeric" : 10,
            "wis_numeric" : 10,
            "cha_numeric" : 10,
            "average_damage" : get_average_damage_no_print(dice_dict=yellow_ninja_dice_dict),
            "attack_modifier" : 5,
            "limited_use_damage" : get_average_damage_no_print(dice_dict=yellow_ninja_bomb_damage),
        }
    yellow_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=yellow_ninja_dictionary,tab_amount=tab_amount)
    return yellow_ninja_cr

def get_green_ninja_cr(tab_amount="\t"):
    print(tab_amount,"get_green_ninja_cr")
    green_ninja_dice_dict = \
        {
            8 : 1,
            "constant" : 4
        }
    green_ninja_dictionary = \
        {
            "ac" : 12,
            "hp" : 15,
            "speed, ground" : 30,
            "str_numeric" : 12,
            "dex_numeric" : 14,
            "con_numeric" : 10,
            "int_numeric" : 12,
            "wis_numeric" : 10,
            "cha_numeric" : 10,
            "average_damage" : get_average_damage_no_print(dice_dict=green_ninja_dice_dict),
            "attack_modifier" : 3,
        }
    green_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=green_ninja_dictionary,tab_amount=tab_amount)
    return green_ninja_cr

#once i use the functions above for the first time i manually put them in the database
#that's why i don't call them in the dungeon function.

def intro_the_turtle_hideout(intro_the_turtle_hideout_calvin_tab_amount="\t"):
    print(intro_the_turtle_hideout_calvin_tab_amount, "intro_the_turtle_hideout")
    intro_the_turtle_hideout_calvin_tab_amount += "\t"

    player_levels = [4,4,4,4]

    #TODO: **maybe** ask a clanker how to make getting the strings easier
    purple_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,
                                                         string="Purple Foot Clan Ninja",
                                                         tab_amount=tab_amount)
    purple_ninja_xp = get_xp_from_single_enemy_cr(cr=purple_ninja_cr,tab_amount=tab_amount)
    lvl_1_monster_xps = \
        [
            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, purple_ninja_xp,
            purple_ninja_xp, purple_ninja_xp, purple_ninja_xp, purple_ninja_xp
        ]
    lvl_1_executioner_difficulty = get_encounter_difficulty(player_levels=player_levels, monster_xp_values=lvl_1_monster_xps, tab_amount=tab_amount)
    print(tab_amount,"calculations complete :-DDD")
    print_dictionary_nicely(dict_in_question=lvl_1_executioner_difficulty,tab_amount=tab_amount)

if __name__ == "__main__":
    tab_amount = "\t"
    intro_the_turtle_hideout()
