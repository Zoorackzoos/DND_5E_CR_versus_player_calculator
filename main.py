import csv

with open('monsters_and_CR.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # Optional: skip the header row
    array = [row for row in reader]
    print(array)