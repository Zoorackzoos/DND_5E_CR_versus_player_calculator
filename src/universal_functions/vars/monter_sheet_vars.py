from src.universal_functions.spreadsheet_stuff.get_array_from_csv_file import get_array_from_csv_file

tab_amount = "\t"
path_to_csv_file = "../../../sheets/monsters_all_stats.csv"

monsters_all_stats_var = get_array_from_csv_file(path_to_csv_file=path_to_csv_file,tab_amount=tab_amount)