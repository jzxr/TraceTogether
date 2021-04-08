import csv
import os
import datetime

class Node:
    # Key is Date
    key = 0
    # Value is Phone Number
    value = 0
    next = None

    def __init__(self, key, value):
        # key is the date 
        self.key = key
        # value is the phone number 
        self.value = value


class HashMap:
    # Date Range: 20/1/2021 to 13/2/21
    dateBase = datetime.datetime(2021,2,13)
    dateRange = list()

    def __init__(self):
        # Size is 25; cause storing contact tracing for 25 days
        self.size = 25
        # Flag for Probing of Date
        self.flag = [False for x in range(self.size)]
        self.key = dict()
        # Array for storing Dates
        self.st = [None for x in range(self.size)]
        self.collectionofDates()
        # Set keys for HashMap for the 25 days
        self.setKey()

    # Get the previous 14days based on user input
    def collectionofDates(self):
        for i in range(self.size):
            newDate = HashMap.dateBase - datetime.timedelta(days=i)
            HashMap.dateRange.append(int(newDate.strftime('%d%m%Y')))
    
    # Linear Probing for Date 
    def setKey(self):
        for i in range(len(HashMap.dateRange)):
            counter = 0
            while self.flag[(HashMap.dateRange[i] % self.size) + counter] is True:
                if ((HashMap.dateRange[i] % self.size) + counter) < self.size - 1:
                    counter += 1
                else:
                    counter -= self.size - 1
            self.key[HashMap.dateRange[i]] = (HashMap.dateRange[i] % self.size) + counter
            self.flag[(HashMap.dateRange[i] % self.size) + counter] = True

    # Get HashMap Keys
    def getkeys(self):
        return self.key

    # Get Key of Date
    def getKey(self, date):
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
        date =(int(date.strftime('%d%m%Y')))
        key = self.key.get(date)
        if key is not None:    
            return key
        else:
            print("Key", date ,"does not exist")

    def put(self, key, value):
        k = self.getKey(key)
        if k is not None:
            node = self.st[k]
            while node is not None:
                # Check for duplicates
                if node.value == value:
                    return
                node = node.next
            #Insert new Node at the front of list
            node = Node(key, value)
            node.next = self.st[k]
            self.st[k] = node
        else:
            return

    def printHashMap(self):
        # list out keys and values separately
        # Reference: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
        key_list = list(self.key.keys())
        val_list = list(self.key.values())

        for i in range(len(self.st)):
            temp = self.st[i]
            print(key_list[val_list.index(i)], end=": ")
            if temp == None:
                print("None", end="")
            while temp is not None:
                print(temp.value, end=", ")
                temp = temp.next
            print()

    # Write HashMap to Csv
    def writeToCsv(self, newHash, filename):
        with open(filename, mode='w') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator = "\n")
            for i in range(len(newHash.st)):
                newList = list()
                temp = newHash.st[i]
                if temp == None:
                    continue
                else:
                    while temp is not None:
                        newList.append(temp.value)
                        temp = temp.next
                    # Get Date of the Hash Map
                    newList.insert(0, str(newHash.st[i].key).split(" ")[0])
                    data_writer.writerow(newList)
