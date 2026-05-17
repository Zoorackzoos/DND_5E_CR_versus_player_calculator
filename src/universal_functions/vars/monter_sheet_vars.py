#from src.universal_functions.spreadsheet_stuff.get_array_from_csv_file import get_array_from_csv_file
from src.universal_functions.spreadsheet_stuff.get_dict_from_csv_file import get_dict_from_csv

tab_amount = "\t"
path_to_csv_file = "../../../sheets/monsters_all_stats.csv"

#monsters_all_stats_array = get_array_from_csv_file(path_to_csv_file=path_to_csv_file, tab_amount=tab_amount)
monsters_all_stats_dict = get_dict_from_csv(function_path_to_csv_file=path_to_csv_file, tab_amount=tab_amount)