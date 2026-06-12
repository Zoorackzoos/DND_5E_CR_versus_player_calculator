import csv

from src.universal_functions.display.print_2d_list_that_contains_dictionaries import \
    print_2d_list_that_contains_dictionaries


def get_dict_from_csv_file(path_to_csv_file, tab_amount="\t"):
    """
    this converts the entire spreadsheet into a dictionary file
    the path_to_csv_file IS a requirement because of the function's feature.
        in any other function, path_to_csv_file is a limitation of my knowledge

    it's important to know this has a worse sister function of
    "get_array_from_csv_file".
        dictionaries are better than arrays in this project.

    :param path_to_csv_file:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_dict_from_csv")
    tab_amount += "\t"
    print(tab_amount,"path_to_csv_file = \n", tab_amount, path_to_csv_file)

    try:
        with open(path_to_csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(tab_amount,"path_to_csv_file = \n", path_to_csv_file)
        exit("ERROR: get_dict_from_csv: shit path_to_csv_file. please put the path to it given the nested dungeon file.")

if __name__ == "__main__":
    path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    # list -> dict
    print_2d_list_that_contains_dictionaries(get_dict_from_csv_file(path_to_csv_file=path_to_csv_file))