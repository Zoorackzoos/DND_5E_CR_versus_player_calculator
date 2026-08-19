def print_2d_list(list_in_question,tab_amount=""):
    for row in list_in_question:
        for element in row:
            print(tab_amount,element, end=" ")
        print()