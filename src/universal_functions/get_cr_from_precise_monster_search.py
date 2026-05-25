from src.universal_functions.spreadsheet_stuff.get_dict_from_csv_file import get_dict_from_csv
from src.universal_functions.spreadsheet_stuff.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from src.universal_functions.vars.monter_sheet_vars import default_path_monsters_all_stats_dict


def get_cr_from_precise_monster_search(param_type, string, path_to_csv_file=default_path_monsters_all_stats_dict, tab_amount="\t"):
    global monster_row
    print(tab_amount,"get_cr_from_monster")
    tab_amount += "\t"
    if path_to_csv_file == default_path_monsters_all_stats_dict:
        monster_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=default_path_monsters_all_stats_dict,
                                                                  param_type=param_type,
                                                                  string=string,
                                                                  get_rows_tab_amount=tab_amount)[0]
    elif path_to_csv_file != default_path_monsters_all_stats_dict:
        monster_row = get_rows_from_dict_on_param_type_and_string(dict_in_question=get_dict_from_csv(path_to_csv_file=path_to_csv_file, tab_amount=tab_amount),
                                                                  param_type=param_type,
                                                                  string=string,
                                                                  get_rows_tab_amount=tab_amount)[0]
    else:
        print("ERROR: get_cr_from_precise_monster_search: finding the .csv file is all fucked up.")
    print(tab_amount,"monster_row:")
    print(tab_amount+"\t",monster_row)
    monster_cr = float(monster_row["CR"])
    print(tab_amount,"monster_cr :",monster_cr)
    return monster_cr