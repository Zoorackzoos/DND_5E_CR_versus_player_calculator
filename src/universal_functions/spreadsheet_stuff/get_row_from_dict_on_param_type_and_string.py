from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict


def get_row_from_dict_on_param_type_and_string(dict_in_question, param_type, string, tab_amount="\t"):
    print(tab_amount,"get_row_from_dict_on_param_type_and_string")
    tab_amount += "\t"

    return_rows = []

    #print(tab_amount,dict_in_question[0].keys())
    #print(tab_amount,dict_in_question[0].values())
    for i in range(len(dict_in_question)):
        if param_type in dict_in_question[i]:
            if string.lower() == dict_in_question[i][param_type].lower():
                return_rows.append(dict_in_question[i])
    print(tab_amount,"the string \"",string,"\" showed up",len(return_rows),"times in the param_type",param_type)

    return return_rows

if __name__ == "__main__":
    tab_amount = "\t"
    get_row_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict, param_type="Type", string="Humanoid", tab_amount=tab_amount)