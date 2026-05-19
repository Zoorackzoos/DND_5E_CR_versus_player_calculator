from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.craft_cr_from_monster_stat_block import plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_damage_per_round import get_damage_per_round_no_print
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.stats.convert_monster_modifiers_to_stats import convert_monster_modifiers_to_stats
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


def intro_the_turtle_hideout(intro_the_turtle_hideout_calvin_tab_amount="\t"):
    print(intro_the_turtle_hideout_calvin_tab_amount, "intro_the_turtle_hideout")
    intro_the_turtle_hideout_calvin_tab_amount += "\t"

    player_levels = [4,4,4,4]

    #it's impossible to not put a string literal as the name.
    #if for some reason you can't get the string, you can search the database using a function.
    bandit_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,string="NPC, Bandit",tab_amount=tab_amount)
    bandit_xp = get_xp_from_single_enemy_cr(cr=bandit_cr,tab_amount=tab_amount)
    lvl_1_monsters_list = [bandit_xp,bandit_cr,
                           bandit_xp,bandit_xp,
                           bandit_cr,bandit_xp,
                           bandit_cr,bandit_xp]
    lvl_1_encounter_difficulty = get_encounter_difficulty(player_levels=player_levels,monster_xp_values=lvl_1_monsters_list,get_encounter_difficulty_tab_amount=tab_amount)

    print_dictionary_nicely(dict_in_question=lvl_1_encounter_difficulty,tab_amount=tab_amount)

if __name__ == "__main__":
    tab_amount = "\t"
    intro_the_turtle_hideout()
