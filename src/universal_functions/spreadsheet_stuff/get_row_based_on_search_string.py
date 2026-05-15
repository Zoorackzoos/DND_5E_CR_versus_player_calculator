def get_row_based_on_search_string(search_string,array_in_question,tab_amount="\t"):
    print(tab_amount,"get_row_based_on_search_string")
    tab_amount += "\t"
    print(tab_amount,"search_string =",search_string)
    #print(tab_amount,"array_in_question = ",array_in_question)

    return_rows = []

    print(tab_amount,"entering loop")
    for i in range(len(array_in_question)):
        #print(tab_amount+"\t",i)
        for element in array_in_question[i]:
            #print(tab_amount+"\t\t",element)
            if search_string.lower() == element.lower():
                return_rows.append(array_in_question[i])

    print(tab_amount,"amount of times",search_string,"was seen = ",len(return_rows))
    return return_rows