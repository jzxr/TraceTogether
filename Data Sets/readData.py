import csv
with open('88877112_SE.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)