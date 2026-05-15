import csv

from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely


def get_dict_from_csv(path_to_csv_file,tab_amount="\t"):
    print(tab_amount,"get_dict_from_csv")

    with open(path_to_csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == "__main__":
    path_to_csv_file = "../../../sheets/monsters_all_stats.csv"
    # list -> dict
    print_2d_list(get_dict_from_csv(path_to_csv_file=path_to_csv_file))