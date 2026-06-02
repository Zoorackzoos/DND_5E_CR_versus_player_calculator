def get_stringified_list_of_enums(list_of_enums, tab_amount="\t"):
    print(tab_amount,"get_stringified_list_of_enums")
    tab_amount += "\t"

    total_string = ""

    for i in range(len(list_of_enums)):
        if i == len(list_of_enums)-1:
            total_string += str(list_of_enums[i])
        else:
            total_string += str(list_of_enums[i]) + ", "

    return total_string