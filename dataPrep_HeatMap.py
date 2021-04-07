import pathlib
import csv
from DataStructuresandAlgorithms.linked_list import LinkedList

def insertLocation():
    newList = LinkedList()
    newList.insertAtHead("BALESTIER PLAZA", 103.850723, 1.325601)
    newList.insertAtHead("CITY SQUARE MALL", 103.850949, 1.280095)
    newList.insertAtHead("NORTHPOINT", 103.836127, 1.42952)
    newList.insertAtHead("SIT-NYP", 103.848787, 1.377433)
    newList.insertAtHead("ZHONGSHAN MALL", 103.8464, 1.3271)
    newList.insertAtHead("APERIA MALL", 103.8644, 1.3101)
    newList.insertAtHead("JCUBE", 103.7402, 1.3333)
    newList.insertAtHead("JURONG POINT", 103.7090, 1.3404)
    newList.insertAtHead("PIONEER MALL", 103.6974, 1.3421)
    return newList

def processing(newList):
    root = pathlib.Path("Data Sets/Results/")
    readfile = "WriteToHtml.csv"
    readdirectory = root / readfile
    writefile = "potential.csv"
    writedirectory = root / writefile
    with open(readdirectory, mode='r') as read_file, open(writedirectory, mode='w') as write_file:
        headers = ['Date', 'Phone-Number', 'Location', 'Degree Contact', 'Longtitute', 'Latitute', 'Interval', 'Weight']
        csv_read = csv.DictReader(read_file)
        csv_write = csv.writer(write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(headers)
        for row in csv_read:
            location_node = newList.search(row["Location"])
            csv_write.writerow([row["Date"], row["Phone-Number"], row["Location"], row["Degree Contact"], location_node.longtitute, location_node.latitute, 0, 1])

def data_prep():
    newList = insertLocation()
    processing(newList)