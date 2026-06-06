from src.universal_functions.display.print_encounter_difficulty_concisely import print_encounter_difficulty_concisely
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_cr_values import \
    get_encounter_difficulty_from_cr_values
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_xp_values import get_encounter_difficulty_from_xp_values
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.vars import spreadsheet_enums
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

into_the_magic_spire_path_to_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def intro_the_magic_spire(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_spire")
    player_levels = [5,5,5,5]

    #manes_smokoer_encounter
    manes_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Demon, Manes",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    manes_smoke_break_cr_values = [manes_cr, manes_cr, manes_cr, manes_cr]
    manes_smoke_break_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=manes_smoke_break_cr_values,
        encounter_name="manes_smoke_break",
        tab_amount=tab_amount
    )

    #mainframe room
    calculus_monster_limit_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Limit",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    calculus_monster_dervative_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Calculus Monster, Derivative",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    withering_gnoll_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Gnoll Witherling",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    mainframe_room_cr_values = \
        [
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_limit_cr, calculus_monster_limit_cr, calculus_monster_limit_cr,
            calculus_monster_dervative_cr,
            withering_gnoll_cr
        ]
    mainframe_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=mainframe_room_cr_values,
        encounter_name="mainframe_room",
        tab_amount=tab_amount
    )

    #office room
    dreadlock_wight_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Deathlock Wight",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    office_room_cr_values = \
        [
            dreadlock_wight_cr
        ]
    office_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=office_room_cr_values,
        encounter_name="office_room",
        tab_amount=tab_amount
    )

    print("\n",tab_amount,"Calculations complete")
    encounter_difficulty_list = \
    [
        manes_smoke_break_encounter_difficulty,
        mainframe_room_encounter_difficulty,
        office_room_encounter_difficulty
    ]
    for encounter in encounter_difficulty_list:
        print(tab_amount+"\t",encounter["encounter_name"])
        print_encounter_difficulty_concisely(dict_in_question=encounter,tab_amount=tab_amount+"\t")

if __name__ == "__main__":
    intro_the_magic_spire()