def print_dictionary_nicely(dict_in_question, tab_amount="\t"):
    print(tab_amount,"print_dictionary_nicely")
    tab_amount += "\t"

    for key,value in dict_in_question.items():
        print(tab_amount,key,":",value)