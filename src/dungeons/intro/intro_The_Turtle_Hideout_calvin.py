from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_array_header import print_array_header_and_array_piece
from src.universal_functions.spreadsheet_stuff.get_row_from_array_based_on_search_string import get_row_from_array_based_on_search_string
from src.universal_functions.spreadsheet_stuff.get_row_from_dict_on_param_type_and_string import \
    get_row_from_dict_on_param_type_and_string
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict


def intro_the_Turtle_Hideout_calvin(tab_amount="\t"):
    print(tab_amount,"intro_the_Turtle_Hideout_calvin")
    tab_amount += "\t"

    player_levels = [3,3,3,3]
    all_humanoids = get_row_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,param_type="Type",string="humanoid",tab_amount=tab_amount)

    """
    how to sort lists of dicts
        don't ask bruh
    the key contains the key it sorts by
    reverse is if you want top to bottum or bottum to top
    """
    all_humanoids.sort(
        key=lambda row: float(row["CR"]),
        reverse=True
    )

    print_2d_list(list_in_question=all_humanoids, tab_amount=tab_amount)


if __name__ == "__main__":
    intro_the_Turtle_Hideout_calvin()
