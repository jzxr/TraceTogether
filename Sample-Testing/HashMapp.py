# Missing
'''
Read CSV
Reload everyday
'''
import datetime
import csv
import os
import pathlib import Path

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
    size = 25
    dateBase = datetime.datetime(2021, 2, 13)
    dateRange = list()

    def __init__(self):
        # Size is 25; cause 25 days
        self.size = HashMap.size
        # Flag for Linear Probing of Date
        self.flag = [False for x in range(self.size)]
        self.key = dict()
        self.st = [None for x in range(self.size)]
        # Get 25 Days
        self.putDate()
        # Set keys for the 25 days
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
            self.key[HashMap.dateRange[i]] = (
                HashMap.dateRange[i] % self.size) + counter
            self.flag[(HashMap.dateRange[i] % self.size) + counter] = True

    # Get Key of Date
    def getKey(self, date):
        date = int(date.strftime('%Y%m%d'))
        key = self.key.get(date)
        if key is not None:
            return key
        else:
            print("Key", date, "does not exist")

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
    # "Qualify" the potentials and filter them with check-in date, check-in time, check-out time
    def SearchContacted(self, arr):
        # path to the root directory to search
        root_dir = "/Users/jasminezheng/Desktop/SIT/CSC1008 Data Structure and Algorithm /Group2_TraceTogether/TraceTogether/Data Sets/Location SE Data"
        # walk the root dir
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:  # iterate over the files in the current dir
                file_path = os.path.join(root, filename)  # build the file path
                try:
                    with open(file_path, "rb") as f:  # open the file for reading
                        # read the file line by line
                        # use: for i, line in enumerate(f) if you need line numbers
                        for line in f:
                            try:
                                # try to decode the contents to utf-8
                                line = line.decode("utf-8")
                            except ValueError:  # decoding failed, skip the line
                                continue
                            if phone_number in line:  # if the infected exists on the current line...
                                # print(file_path)  # print the file path
                                # break  # no need to iterate over the rest of the file
                                for i in range(len(arr[0])):
                                    with open(file_path, mode='r') as f:
                                        reader = csv.DictReader(f)
                                        line_count = 0

                                        try:
                                            for row in reader:
                                                if line_count < 1:
                                                    line_count += 1
                                                if arr[0][i] != row["Phone No."]:
                                                    checkintime = datetime.datetime.strptime(
                                                        row["Check-in date"] + " " + row["Check-in time"], "%d/%m/%Y %H%M")
                                                    checkoutime = datetime.datetime.strptime(
                                                        row["Check-in date"] + " " + row["Check-out time"], "%d/%m/%Y %H%M")
                                                    # print(checkintime, " ", checkoutime)

                                                    # Check for infected
                                                    if (checkoutime > arr[3][i] or checkintime < arr[2][i]):
                                                        continue
                                                    else:
                                                        try:
                                                            self.put(datetime.datetime.strptime(
                                                                row["Check-in date"], '%d/%m/%Y').date(), row["Phone No."])
                                                        except ValueError:
                                                            print(
                                                                row["Check-in date"], 'Date does not exist')
                                        except csv.Error as e:
                                            sys.exit('file {}, line {}: {}'.format(
                                                filename, reader.line_num, e))
                                    break
                                else:
                                    print("Phone not found in path.")
                except (IOError, OSError):  # ignore read and permission errors
                    pass

    # Write HashMap to csv
    def writeToTTCsv(self):
        # file name needs to be replaced with phone number
        with open('TraceTogether/Data Sets/TraceTogether/'+phone_number+'_TT.csv', mode='w') as data_file:
            data_writer = csv.writer(
                data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.st)):
                potentialList = list()
                temp = self.st[i]
                if temp == None:
                    continue
                else:
                    while temp is not None:
                        potentialList.append(temp.value)
                        temp = temp.next
                    # Get key from first element in the Hash Map
                    potentialList.insert(0, self.st[i].key)
                    data_writer.writerow(potentialList)

    # Searching Algo: Using a Simple Linear search using 3 list
    def selectFromCsv(self, phone_number):
        phonenumberlist = list()
        locationlist = list()
        starttimelist = list()
        endtimelist = list()
        # path to the root directory to search
        root_dir = "/Users/jasminezheng/Desktop/SIT/CSC1008 Data Structure and Algorithm /Group2_TraceTogether/TraceTogether/Data Sets/Location SE Data"
        # walk the root dir
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:  # iterate over the files in the current dir
                file_path = os.path.join(root, filename)  # build the file path
                try:
                    with open(file_path, "rb") as f:  # open the file for reading
                        # read the file line by line
                        # use: for i, line in enumerate(f) if you need line numbers
                        for line in f:
                            try:
                                # try to decode the contents to utf-8
                                line = line.decode("utf-8")
                            except ValueError:  # decoding failed, skip the line
                                continue
                            if phone_number in line:  # if the infected exists on the current line...
                                # print(file_path)  # print the file path
                                # break  # no need to iterate over the rest of the file

                                with open(file_path, mode='r') as f:
                                    reader = csv.DictReader(f)
                                    line_count = 0
                                    potential = list()
                                    try:
                                        for row in reader:
                                            if line_count < 1:
                                                line_count += 1
                                            # Read data from each row
                                            if row["Phone No."] == phone_number:

                                                starttime = datetime.datetime.strptime(
                                                    row["Check-in date"] + " " + row["Check-in time"], "%d/%m/%Y %H%M")
                                                endtime = datetime.datetime.strptime(
                                                    row["Check-in date"] + " " + row["Check-out time"], "%d/%m/%Y %H%M")

                                                print(starttime, " ", endtime)

                                                phonenumberlist.append(phone_number)
                                                locationlist.append(file_path)
                                                starttimelist.append(starttime)
                                                endtimelist.append(endtime)
                
                                        potentialList = [phonenumberlist, locationlist, starttimelist, endtimelist]
                                        return potentialList
                                    except csv.Error as e:
                                        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
                                break
                            else:
                                print("Phone not found in path.")
                except (IOError, OSError):  # ignore read and permission errors
                    pass

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
                print(temp.value, end=", ")
                temp = temp.next
            print()

    def open_TTFile(self):
        # path to the root directory to search
        root_dir = "/Users/jasminezheng/Desktop/SIT/CSC1008 Data Structure and Algorithm /Group2_TraceTogether/TraceTogether/Data Sets/TraceTogether"
        TTList = list()
        # walk the root dir
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:  # iterate over the files in the current dir
                file_path = os.path.join(root, filename)  # build the file path
                try:
                    with open(file_path, "rb") as f:  # open the file for reading
                        # read the file line by line
                        # use: for i, line in enumerate(f) if you need line numbers
                        for line in f:
                            try:
                                # try to decode the contents to utf-8
                                line = line.decode("utf-8")
                            except ValueError:  # decoding failed, skip the line
                                continue
                            if phone_number in file_path:  # if the infected exists on the current line...
                                with open(file_path, mode='r') as f:
                                    CTreader = csv.DictReader(f)
                                    try:
                                        for row in CTreader:
                                            TTList.append(row)
                                            # for i in range(0,len(storeAllList)):
                                            #     if TTList in storeAllList[i][0]:
                                        # print(TTList)
                                        return TTList
                                    except csv.Error as e:
                                        sys.exit('file {}, line {}: {}'.format(
                                            filename, CTreader.line_num, e))
                            else:
                                print("Phone not found in path.")
                except (IOError, OSError):  # ignore read and permission errors
                    pass

    # Find the direct contact from the potentials and compare the "potentials"_CT.csv
    def findDirectContact(self, phone_number):
        # path to the root directory to search
        root_dir = "/Users/jasminezheng/Desktop/SIT/CSC1008 Data Structure and Algorithm /Group2_TraceTogether/TraceTogether/Data Sets/Contact Tracing"

        storeAllList = list()
        dateList = list()
        personList = list()
        TTList = list()
        directContactList = list()

        # walk the root dir
        for root, dirs, files in os.walk(root_dir, onerror=None):
            for filename in files:  # iterate over the files in the current dir
                file_path = os.path.join(root, filename)  # build the file path
                try:
                    with open(file_path, "rb") as f:  # open the file for reading
                        # read the file line by line
                        # use: for i, line in enumerate(f) if you need line numbers
                        for line in f:
                            try:
                                # try to decode the contents to utf-8
                                line = line.decode("utf-8")
                            except ValueError:  # decoding failed, skip the line
                                continue
                            if phone_number in file_path:  # if the infected exists on the current line...
                                with open(file_path, mode='r') as f:
                                    CTreader = csv.DictReader(f)
                                    try:
                                        for row in CTreader:
                                            personList.append(row)
                                            personList = line.split(',')
                                        for i in range(1, 9):
                                            storeAllList.append(
                                                personList[i].split(':'))
                                        #dateList.append(personList[0])

                                    except csv.Error as e:
                                        sys.exit('file {}, line {}: {}'.format(
                                            filename, reader.line_num, e))

                except (IOError, OSError):  # ignore read and permission errors
                    pass

        for i in range(0, len(storeAllList)):
            # determine the potential list by their distance.
            # if distance at least 2m, and up to 5m.
            phone_number = storeAllList[i][0]
            dist = int(storeAllList[i][1])
            timeWindow = int(storeAllList[i][2])
            if 2 >= dist < 5:
                if timeWindow < 30:
                    directContactList = phone_number

        with open('TraceTogether/Data Sets/Contact Tracing/'+str(phone_number)+'_DirectContact_infected.csv', mode='w') as data_file:
            data_writer = csv.writer(
                data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.st)):
                directContactList = list()
                temp = self.st[i]
                if temp == None:
                    continue
                else:
                    while temp is not None:
                        directContactList.append(temp.value)
                        temp = temp.next
                    # # Get key from first element in the Hash Map
                    # infectedList.insert(0, self.st[i].key)
                    data_writer.writerow(directContactList)

        print("end of CT data")

    #Find the indirect contact from the potentials
    def findIndirectContact(self):
        
        direct_phone = []
        with open('TraceTogether/Data Sets/Contact Tracing/DirectContact_infected.csv', mode='r') as data_file:
            data_reader = csv.reader(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in data_reader:
                for col in row:
                    direct_phone = col
                    print(direct_phone)
                    indirectHash = HashMap()
                    indirectArr = newHash.selectFromCsv(direct_phone)
                    newHash.SearchContacted(indirectArr)
                    print()
                    newHash.print()
                    newHash.writeToTTCsv()
                    newHash.findDirectContact(direct_phone)

newHash = HashMap()

# Step 1. Choose Infected Phone Number
phone_number = input("Enter the infected person's number: ")

# Step2. Get Check in and Check out from Infected person
arr = newHash.selectFromCsv(phone_number)

# Step 3. Search for people who enter mall within the time range of infected person
newHash.SearchContacted(arr)
print()

# Print Result to console
newHash.print()

# Step 4. Write Potentials Result to TraceTogether csv
newHash.writeToTTCsv()

# Step 5. Search for people who are within close proximity - Direct Contact
newHash.findDirectContact(phone_number)

newHash.findIndirectContact()
