# Missing 
''' 
Read CSV 
Reload everyday
'''
import datetime
import csv

class Node:
    key = 0
    value = 0
    next = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    size = 25
    dateBase = datetime.date.today()
    dateRange = list()

    def __init__(self):
        self.size = HashMap.size
        self.flag = [False for x in range(self.size)]
        self.key = dict()
        self.st = [None for x in range(self.size)]
        self.putDate()
        self.setKey()

    def putDate(self):
        for i in range(self.size):
            newDate = HashMap.dateBase - datetime.timedelta(days=i)
            HashMap.dateRange.append(int(newDate.strftime('%Y%m%d')))
 
    # Linear Probing
    def setKey(self):
        for i in range(len(HashMap.dateRange)):
            counter = 0
            while self.flag[(HashMap.dateRange[i] % self.size) + counter] is True:
                counter += 1
            self.key[HashMap.dateRange[i]] = (HashMap.dateRange[i] % self.size) + counter
            self.flag[(HashMap.dateRange[i] % self.size) + counter] = True
    
    def getKey(self, date):
        date = int(date.strftime('%Y%m%d'))
        key = self.key.get(date)
        if key is not None:    
            return key
        else:
            print("Key does not exist")

    def printKey(self):
        print(self.key)

    def put(self, key, value):
        k = self.getKey(key)
        if k is not None:
            node = self.st[k]
            while node is not None:
                # Key exist
                if node.value == value:
                    return
                node = node.next
            node = Node(key, value)
            node.next = self.st[k]
            self.st[k] = node
        else:
            return

    def writeToCsv(self):
        with open('data.csv', mode='w') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.st)):
                newList = list()
                temp = self.st[i]
                if temp == None:
                    continue
                else: 
                    while temp is not None:
                        newList.append(temp.value)
                        temp = temp.next
                    newList.insert(0, self.st[i].key)
                    data_writer.writerow(newList)

    def print(self):
        for i in range(len(self.st)):
            temp = self.st[i]
            if temp == None:
                print("None", end="")
            while temp is not None:
                print(temp.value, end = ", ")
                temp = temp.next
            print()

    
newHash = HashMap()

newHash.put(datetime.date(2021, 3, 13), "97601182")
newHash.put(datetime.date(2021, 3, 13), "97601183")
newHash.put(datetime.date(2021, 3, 12), "97601184")
newHash.put(datetime.date(2021, 3, 11), "97601185")
newHash.put(datetime.date(2021, 3, 10), "97601186")
newHash.put(datetime.date(2021, 2, 18), "97601187")

newHash.put(datetime.date(2021, 3, 20), "97601187")
print()
newHash.print()
newHash.writeToCsv()
