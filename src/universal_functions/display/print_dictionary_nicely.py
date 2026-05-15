def print_dictionary_nicely(dict,tab_amount="\t"):
    print(tab_amount,"print_dictionary_nicely")
    tab_amount += "\t"

    for key,value in dict.items():
        print(tab_amount,":",key,value)