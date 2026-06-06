def print_2d_list_that_contains_dictionaries(list_dict_variable, tab_amount="\t"):

    if len(list_dict_variable) == 0:
        print(tab_amount, "empty list_dict_variable")
        return

    headers = list_dict_variable[0].keys()

    # Calculate max width of each column
    column_widths = {}

    for header in headers:
        #anything in the spreadsheet, or spreadsheets will be a string.
        #however if you had a int as a key instead, this would make sure
        # the function doesn't blow up
        max_width = len(str(header))

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
    list_of_dice_dicts = \
        [
            {
                20: 1,
                12: 1,
                10: 1,
                8: 1,
                6: 1,
                4: 1,
                "constant": 1
            },
            {
                20: 2,
                12: 2,
                10: 2,
                8: 2,
                6: 2,
                4: 2,
                "constant": 2
            }
        ]
    print_2d_list_that_contains_dictionaries(
        list_dict_variable=list_of_dice_dicts,
        tab_amount=tab_amount
    )