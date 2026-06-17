from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.vars import spreadsheet_enums
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums

player_levels = [6, 6, 6, 6]
path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def phase_1_michelangelo_the_dmv_lvl_1(tab_amount="\t"):
    """
    i hate abbreviations. so instead of hthq it's instead the DMV.
    i am not putting the words ht stands for in my repo dammit

    :param tab_amount:
    :return:
    """
    print(tab_amount,"phase_1_michelangelo_the_dmv_lvl_1")
    tab_amount += "\t"

    """
    the office
    6 purple ninjas
    1 pink ninja
    """
    purple_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 purple foot clan ninja",
        path_to_csv_file=path_to_csv_file,
        tab_amount=tab_amount
    )
    pink_ninja_cr = get_cr_from_precise_monster_search(
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="phase 1 pink ninja clan ninja",
        path_to_csv_file=path_to_csv_file,
        tab_amount=tab_amount
    )
    phase_1_michelangelo_the_dmv_lvl_1_the_office

    pass

if __name__ == "__main__":
    tab_amount="\t"
    phase_1_michelangelo_the_dmv_lvl_1(tab_amount=tab_amount)