# Missing 
''' 
Read CSV 
Reload everyday
'''
import datetime
import csv

class Node:
    #Key is Date
    key = 0
    #Value is Phone Number
    value = 0
    next = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    size = 25
    dateBase = datetime.datetime(2021, 2, 13)
    dateRange = list()

    def __init__(self):
        self.size = HashMap.size
        self.flag = [False for x in range(self.size)]
        self.key = dict()
        self.st = [None for x in range(self.size)]
        self.putDate()
        self.setKey()

    # Store today-constant to today date in array
    def putDate(self):
        for i in range(self.size):
            newDate = HashMap.dateBase - datetime.timedelta(days=i)
            HashMap.dateRange.append(int(newDate.strftime('%Y%m%d')))
 
    # Linear Probing: Map Date to Key
    def setKey(self):
        for i in range(len(HashMap.dateRange)):
            counter = 0
            while self.flag[(HashMap.dateRange[i] % self.size) + counter] is True:
                # If Flag is within array bound
                if ((HashMap.dateRange[i] % self.size) + counter) < self.size - 1:
                    counter += 1
                # Else reset to first index of flag
                else:
                    counter -= self.size - 1
            self.key[HashMap.dateRange[i]] = (HashMap.dateRange[i] % self.size) + counter
            self.flag[(HashMap.dateRange[i] % self.size) + counter] = True
    
    # Get Key of Date
    def getKey(self, date):
        date = int(date.strftime('%Y%m%d'))
        key = self.key.get(date)
        if key is not None:    
            return key
        else:
            print("Key", date ,"does not exist")

    # Print List of Keys 
    def printKey(self):
        print(self.key)

    # Map phone number to HashMap
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

    # Inefficent Search; using Linear search
    def SearchContacted(self, arr):
        for i in range(len(arr[0])):
            with open('SIT-NYP.csv', mode='r') as csv_file:
                csv_read = csv.DictReader(csv_file)
                # For each check in 
                line_count = 0
                for row in csv_read:
                    #Skip the header
                    if line_count < 1:
                        line_count += 1
                    if arr[0][i] != row["Phone No."]:
                        checkintime = datetime.datetime.strptime(row["Check-in date"] + " " + row["Check-in time"], "%d/%m/%Y %H%M")
                        checkoutime = datetime.datetime.strptime(row["Check-in date"] + " " + row["Check-in time"], "%d/%m/%Y %H%M") 
                        #print(checkintime, " ", checkoutime)
                        if (checkoutime > arr[3][i] or checkintime < arr[2][i]):
                            continue
                        else:
                            try:
                                self.put(datetime.datetime.strptime(row["Check-in date"], '%d/%m/%Y').date(), row["Phone No."])
                            except ValueError:
                                print(row["Check-in date"], 'Date does not exist')

    # Write HashMap to csv
    def writeToCsv(self):
        # file name needs to be replaced with phone number
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
                    # Get key from first element in the Hash Map
                    newList.insert(0, self.st[i].key)
                    data_writer.writerow(newList)

    # Searching Algo: Using a Simple Linear search using 3 list
    def selectFromCsv(self, phone_number):
        phonenumberlist = list()
        locationlist = list()
        starttimelist = list()
        endtimelist = list()
        with open('SIT-NYP.csv', mode='r') as csv_file:
            csv_read = csv.DictReader(csv_file)
            line_count = 0 
            for row in csv_read:
                # Skip header row 
                if line_count < 1:
                    line_count += 1
                # Read data from each row
                if row["Phone No."] == phone_number:
                    starttime = datetime.datetime.strptime(row["Check-in date"] + " " + row["Check-in time"], "%d/%m/%Y %H%M")
                    endtime = datetime.datetime.strptime(row["Check-in date"] + " " + row["Check-out time"], "%d/%m/%Y %H%M")

                    phonenumberlist.append(phone_number)
                    locationlist.append("SIT-NYP")
                    starttimelist.append(starttime)
                    endtimelist.append(endtime)
            newlist = [phonenumberlist, locationlist, starttimelist, endtimelist]
            return newlist

    # Print HasMap to console
    def print(self):
        # list out keys and values separately
        # Reference: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
        key_list = list(self.key.keys())
        val_list = list(self.key.values())

        for i in range(len(self.st)):
            temp = self.st[i]
            # print key with val i
            print(key_list[val_list.index(i)], end=': ')
            if temp == None:
                print("None", end="")
            while temp is not None:
                print(temp.value, end = ", ")
                temp = temp.next
            print()

    
newHash = HashMap()

phone_number = input("Enter phone number of infected person")
phone_number = "81841425"
arr = newHash.selectFromCsv(phone_number)
newHash.SearchContacted(arr)
print()
newHash.print()
newHash.writeToCsv()
