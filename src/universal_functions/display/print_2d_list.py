def print_2d_list(list_in_question, tab_amount="\t"):

    if len(list_in_question) == 0:
        print(tab_amount, "empty list")
        return

    headers = list_in_question[0].keys()

    # Calculate max width of each column
    column_widths = {}

    for header in headers:
        max_width = len(header)

        for row in list_in_question:
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
    for row in list_in_question:

        line = ""

        for header in headers:
            width = column_widths[header]
            line += f"{str(row[header]):<{width}} | "

        print(tab_amount + line)