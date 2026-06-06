from src.universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import get_dict_from_csv_file
from src.universal_functions.vars import spreadsheet_enums


def print_2d_list_that_contains_dictionaries(list_dict_variable, tab_amount="\t"):

    if len(list_dict_variable) == 0:
        print(tab_amount, "empty list_dict_variable")
        return

    headers = list_dict_variable[0].keys()

    # Calculate max width of each column
    column_widths = {}

    for header in headers:
        max_width = len(header)

        for row in list_dict_variable:
            value_length = len(str(row[header]))

            if value_length > max_width:
                max_width = value_length

        column_widths[header] = max_width

    # Print headers
    header_line = ""

    for header in headers:
        width = column_widths[header]
        header_line += f"{header:<{width}} | "

    print(tab_amount + header_line)

    # Print separator
    separator = ""

    for header in headers:
        separator += "-" * column_widths[header] + "-+-"

    print(tab_amount + separator)

    # Print rows
    for row in list_dict_variable:

        line = ""

        for header in headers:
            width = column_widths[header]
            line += f"{str(row[header]):<{width}} | "

        print(tab_amount + line)

if __name__ == "__main__":
    tab_amount = "\t"
    path_to_csv_file = "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    rows_of_humanoids = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=get_dict_from_csv_file
        (
            path_to_csv_file=path_to_csv_file,
            tab_amount=tab_amount+"\t"
        ),
        param_type=spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value,
        string=spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
        tab_amount=tab_amount
    )
    print()
    print_2d_list_that_contains_dictionaries(
        list_dict_variable=rows_of_humanoids,
        tab_amount=tab_amount
    )