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
player_levels = [5, 5, 5, 5]

def intro_the_magic_spire_lvl_1(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_spire_lvl_1")

    #manes_smokoer_encounter
    """
    manes_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Demon, Manes",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    hag_green_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Hag, Green",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    hags_smoke_break_cr_values = \
        [
            hag_green_cr,hag_green_cr,hag_green_cr
        ]
    hags_smoke_break_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=hags_smoke_break_cr_values,
        encounter_name="hags_smoke_break",
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
    """
    dreadlock_wight_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Deathlock Wight",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    """
    embrald_gemstone_guy_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Golem, Gemstone, Emerald",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    office_room_cr_values = \
        [
            embrald_gemstone_guy_cr
        ]
    office_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=office_room_cr_values,
        encounter_name="office_room",
        tab_amount=tab_amount
    )

    print("\n",tab_amount,"intro_the_magic_spire_lvl_1_encounter_difficulty completed")
    intro_the_magic_spire_lvl_1_encounter_difficulty_list = \
    [
        hags_smoke_break_encounter_difficulty,
        mainframe_room_encounter_difficulty,
        office_room_encounter_difficulty
    ]
    for encounter in intro_the_magic_spire_lvl_1_encounter_difficulty_list:
        print(tab_amount+"\t",encounter["encounter_name"])
        print_encounter_difficulty_concisely(dict_in_question=encounter,tab_amount=tab_amount+"\t")

def intro_the_magic_spire_lvl_2(tab_amount="\t"):
    #break room
    troglidyte_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Troglodyte",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    break_room_cr_values = \
    [
        troglidyte_cr, troglidyte_cr
    ]
    break_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=break_room_cr_values,
        encounter_name="break_room",
        tab_amount=tab_amount
    )

    #dining room
    animated_armour_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Animated Object, Armor",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    dining_room_monster_cr_values = \
    [
        animated_armour_cr
    ]
    dining_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=dining_room_monster_cr_values,
        encounter_name="dining_room",
        tab_amount=tab_amount
    )

    #kitchen
    lizard_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Lizard",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    giant_lizard_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Giant Lizard",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    kitchen_cr_values = \
    [
        giant_lizard_cr,
        lizard_cr, lizard_cr
    ]
    kitchen_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=kitchen_cr_values,
        encounter_name="kitchen",
        tab_amount=tab_amount
    )

    #movie room
    wolf_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Wolf",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    movie_room_cr_values = \
    [
        wolf_cr,wolf_cr
    ]
    movie_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=movie_room_cr_values,
        encounter_name="movie_room",
        tab_amount=tab_amount
    )

    #teal key room
    spectator_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Beholder, Spectator",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    teal_key_cr_values = \
        [
            spectator_cr
        ]
    teal_key_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=teal_key_cr_values,
        encounter_name="teal_key",
        tab_amount=tab_amount
    )

    #bottom left conference room
    bottom_left_conference_room_cr_values = \
        [
            wolf_cr,wolf_cr
        ]
    bottom_left_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=bottom_left_conference_room_cr_values,
        encounter_name="bottom_left_conference_room",
        tab_amount=tab_amount
    )

    #flower conference room. official flower busniess
    tri_flower_frond_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Tri-Flower Frond",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    flower_conference_room_cr_values = \
    [
        tri_flower_frond_cr
    ]
    flower_conference_room_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=flower_conference_room_cr_values,
        encounter_name="flower_conference_room",
        tab_amount=tab_amount
    )

    intro_the_magic_spire_lvl_2_encounters_list = \
    [
        break_room_encounter_difficulty,
        dining_room_encounter_difficulty,
        kitchen_encounter_difficulty,
        movie_room_encounter_difficulty,
        teal_key_room_encounter_difficulty,
        bottom_left_encounter_difficulty,
        flower_conference_room_encounter_difficulty,
    ]
    print("\n",tab_amount+"\tintro_the_magic_spire_lvl_2_encounters completed")
    for encounter in intro_the_magic_spire_lvl_2_encounters_list:
        print(tab_amount+"\t\t",encounter["encounter_name"])
        print_encounter_difficulty_concisely(dict_in_question=encounter, tab_amount=tab_amount)

def intro_the_magic_spire_lvl_3(tab_amount="\t"):
    """
    it's just one big barracks.
    cockroach people live in there

    :param tab_amount:
    :return:
    """
    #barracks
    polar_bear_cr = get_cr_from_precise_monster_search(
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.NAME.value,
        string="Misc. Creature, Polar Bear",
        path_to_csv_file=into_the_magic_spire_path_to_csv_file,
        tab_amount=tab_amount
    )
    barracks_cr_value = \
    [
        polar_bear_cr, polar_bear_cr, polar_bear_cr
    ]
    barracks_encounter_difficulty = get_encounter_difficulty_from_cr_values(
        player_levels=player_levels,
        monster_cr_values=barracks_cr_value,
        encounter_name="barracks",
        tab_amount=tab_amount
    )

    intro_the_magic_spire_lvl_3_encounters_list = \
        [
            barracks_encounter_difficulty
        ]
    print("\n", tab_amount + "\tintro_the_magic_spire_lvl_3_encounters completed")
    for encounter in intro_the_magic_spire_lvl_3_encounters_list:
        print(tab_amount + "\t\t", encounter["encounter_name"])
        print_encounter_difficulty_concisely(dict_in_question=encounter, tab_amount=tab_amount+"\t\t\t")

if __name__ == "__main__":
    tab_amount = "\t"
    print("begin program")
    #intro_the_magic_spire_lvl_1(tab_amount=tab_amount)
    intro_the_magic_spire_lvl_2(tab_amount=tab_amount)
    #intro_the_magic_spire_lvl_3(tab_amount=tab_amount)
    print("end program")