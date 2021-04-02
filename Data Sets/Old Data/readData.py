import csv
with open('1000_CT.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)