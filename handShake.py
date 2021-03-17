import csv

def getCsvData():
    with open('trace-together.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def handShake(data):
    for i in range(2,len(data)):
        signal = data[i][8]
    
        


data = getCsvData()
handShake(data)
