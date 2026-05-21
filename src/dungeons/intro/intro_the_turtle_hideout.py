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
            "ability_cr_weight" : 0
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
        }
    blue_ninja_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=blue_ninja_dictionary,tab_amount=tab_amount)
    return blue_ninja_cr

def get_pink_ninja_cr(tab_amount="\t"):

def intro_the_turtle_hideout(intro_the_turtle_hideout_calvin_tab_amount="\t"):
    print(intro_the_turtle_hideout_calvin_tab_amount, "intro_the_turtle_hideout")
    intro_the_turtle_hideout_calvin_tab_amount += "\t"

    player_levels = [4,4,4,4]

    blue_ninja_cr = get_blue_ninja_cr(tab_amount=tab_amount)
    print(blue_ninja_cr)

if __name__ == "__main__":
    tab_amount = "\t"
    intro_the_turtle_hideout()
