def print_array_header_and_array_piece(array_in_question, array_piece, tab_amount="\t"):
    print(tab_amount,"print_array_header")
    tab_amount += "\t"
    print(tab_amount,array_in_question[0])
    for element in array_piece:
        print(tab_amount,element)