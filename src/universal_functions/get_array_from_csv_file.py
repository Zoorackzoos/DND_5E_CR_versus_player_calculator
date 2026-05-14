import csv

from print_2d_list import print_2d_list

def get_array_from_csv_file(path_to_csv_file,tab_amount="\t"):
    print(tab_amount,"get_array_from_csv_file")

    with open(path_to_csv_file, mode='r') as file:
        reader = csv.reader(file)
        #next(reader) # Optional: skip the header row
        array = [row for row in reader]

    return array
