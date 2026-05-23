import csv

from src.universal_functions.display.print_2d_list_that_contains_dictionaries import print_2d_list_that_contains_dictionaries

def get_dict_from_csv(function_path_to_csv_file, tab_amount="\t"):
    print(tab_amount,"get_dict_from_csv")
    tab_amount += "\t"
    print(tab_amount,"path_to_csv_file = \n", tab_amount, function_path_to_csv_file)

    with open(function_path_to_csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == "__main__":
    path_to_csv_file = "../../../sheets/monsters_all_stats.csv"
    # list -> dict
    print_2d_list_that_contains_dictionaries(get_dict_from_csv(function_path_to_csv_file=path_to_csv_file))