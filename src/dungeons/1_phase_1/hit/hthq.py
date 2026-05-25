from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


def hthq(tab_amount="\t"):
    print(tab_amount,"hthq")

    player_levels = [4,4,4,4]

    purple_ninja_cr = get_cr_from_precise_monster_search(param_type=SpreadsheetKeysEnums.NAME.value,string="Purple Foot Clan Ninja",tab_amount=tab_amount)
    print(purple_ninja_cr)
    ground_level_enemies = 0

if __name__ == "__main__":
    hthq()