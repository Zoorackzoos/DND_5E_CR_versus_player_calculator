from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.vars.monter_sheet_vars import monsters_all_stats_dict


def get_cr_from_precise_monster_search(param_type, string, tab_amount="\t"):
    print(tab_amount,"get_cr_from_monster")
    tab_amount += "\t"
    monster_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=monsters_all_stats_dict,
                                                              param_type=param_type,
                                                              string=string,
                                                              get_rows_tab_amount=tab_amount)[0]
    print(tab_amount,"monster_row:")
    print(tab_amount+"\t",monster_row)
    monster_cr = float(monster_row["CR"])
    print(tab_amount,"monster_cr :",monster_cr)
    return monster_cr