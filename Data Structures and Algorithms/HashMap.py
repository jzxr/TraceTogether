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
        self.key = key
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
        # ??? 
        self.key = dict()
        # Array for storing Dates
        self.st = [None for x in range(self.size)]
        self.collectionofDates()
        # Set keys for HashMap for the 25 days
        self.setKey()

    # Get Date Range: 20/1/2021 to 13/2/21
    def collectionofDates(self):
        for i in range(self.size):
            newDate = HashMap.dateBase - datetime.timedelta(days=i)
            HashMap.dateRange.append(int(newDate.strftime('%d%m%Y')))

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
        date = int(date.strftime('%d%m%Y'))
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
            # Insert new Node at the front of list
            node = Node(key, value)
            node.next = self.st[k]
            self.st[k] = node
        else:
            return

    def selectInfected(self, infectedperson):
        check_in_date_arr = list()
        check_in_location_arr = list()
        check_in_time_arr = list()
        check_out_time_arr = list()
        infectedperson_file = infectedperson + "_SE.csv"
        try:
            with open(infectedperson_file, mode='r') as csv_file:
                csv_read = csv.DictReader(csv_file)
                for row in csv_read:
                    # Reformat and Stores all infected person information in arrays
                    infected_checkin_date = datetime.datetime.strptime(row["Check-in date"], "%d/%m/%Y")
                    check_in_date_arr.append(infected_checkin_date)
                    check_in_location_arr.append(row["Check-in location"])
                    infected_checkin_time = datetime.datetime.strptime(row["Check-in time"], "%H%M")
                    check_in_time_arr.append(infected_checkin_time)
                    infected_checkout_time = datetime.datetime.strptime(row["Check-in time"], "%H%M")
                    check_out_time_arr.append(infected_checkout_time)
            arr = [check_in_date_arr, check_in_location_arr, check_in_time_arr, check_out_time_arr]
            return arr
        except Exception as e:
            print(e)


    def SearchContacted(self, arr):
        # REQUIRES EDIT FOR FUTURE USE
        root_dir = "/home/jamestsui/Desktop/project/1008-DS/TT/data"
        for root, dirs, files in os.walk(root_dir, onerror=None):
            # Get filename within the root_dir
            for filename in files:
                # Get Filename without the .csv file type
                temp = filename.split('.')[0]
                # arr[1]: check-in locations of infected
                for i in range(len(arr[1])):
                    # Search for the following condition (location.csv AND infected person location entry)
                    if temp == arr[1][i]:
                        # Open the location.csv file
                        file_path = os.path.join(root, filename)
                        try:
                            with open(file_path, "r") as csv_file:
                                csv_read = csv.DictReader(csv_file)
                                # arr[0][i]: Get Check in date of infected
                                # arr[2][i]: Get Check in timing of infected 
                                # arr[3][i]: Get Check out timing of infected
                                # Reformat check in date as datetime libraray 
                                line_count = 0
                                for row in csv_read:
                                    if line_count < 1:
                                        line_count += 1
                                    else:
                                        normal_checkin_date = datetime.datetime.strptime(row["Check-in date"], "%d/%m/%Y")
                                        normal_checkin_time = datetime.datetime.strptime(row["Check-in time"], "%H%M")
                                        normal_checkout_time = datetime.datetime.strptime(row["Check-out time"], "%H%M")
                                        # Check Condition: Infected person date == Normal person date
                                        if arr[0][i] == normal_checkin_date:
                                            # Check Condition: Normal person time range in within the infected person time range
                                            if (normal_checkout_time < arr[2][i]) or (normal_checkin_time > arr[3][i]):
                                                continue
                                            else:
                                                self.put(normal_checkin_date, row["Phone No."])
                        except Exception as e:
                            print("Error Message")
                            print(e)
    
    # Write HashMap to Csv
    def writeToCsv(self):
        with open('FirstDegree_SE.csv', mode='w') as data_file:
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
                    # Get Date of the Hash Map
                    newList.insert(0, str(self.st[i].key).split(" ")[0])
                    data_writer.writerow(newList)

    
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
            

newHash = HashMap()

infectedperson = input("Enter phone number of the infected person: ")
if len(infectedperson) != 8:
    print("Invalid phone number")
else:
    # Step2. Get Check in and Check out from Infected person
    arr = newHash.selectInfected(infectedperson)
    # Step 3. Search for people who enter mall within the time range of infected person
    newHash.SearchContacted(arr)
    # Print Result to console 
    newHash.printHashMap()
    # Step 4. Write Result to csv 
    newHash.writeToCsv()
