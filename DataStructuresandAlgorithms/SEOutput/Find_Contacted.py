import csv
import os
import datetime
from HashMap import newHash
import pathlib

#################### First Degree Contact Code ############################

def selectInfected(infectedperson, flag):
    check_in_date_arr = list()
    check_in_location_arr = list()
    check_in_time_arr = list()
    check_out_time_arr = list()
    infectedperson_arr = list()
    first_degree_person1 = list()
    first_degree_person2 = list()

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
                if flag is True:
                    infectedperson_arr.append(infectedperson)
                else:
                    first_degree_person1.append(row["Phone Number Check in"])
                    first_degree_person2.append(row["Phone Number Check Out"])

        if flag is True:
            arr = [check_in_date_arr, check_in_location_arr, check_in_time_arr, check_out_time_arr, infectedperson_arr]
            return arr
        else:
            arr = [check_in_date_arr, check_in_location_arr, check_in_time_arr, check_out_time_arr, first_degree_person1, first_degree_person2]
            return arr
    except Exception as e:
        print(e)


def SearchContacted(parentNode, arr, newHash, flag):
    root_dir = str(pathlib.Path().absolute()) + "/data"
    for root, dirs, files in os.walk(root_dir, onerror=None):
        # Get filename within the root_dir
        for filename in files:
            # Get Filename without the .csv file type
            location = filename.split('.')[0]


            # arr[1]: check-in locations of infected
            for i in range(len(arr[1])):
                # Search for the following condition (location.csv AND infected person location entry)
                if location == arr[1][i]:
                    # Open the location.csv file
                    file_path = os.path.join(root, filename)

                    try:

                        # Get information to prep for second degree contact tracing
                        firstdegree_phone_number_check_in = None
                        firstdegree_phone_number_check_out = None
                        seconddegree_checkin_date = None
                        seconddegree_checkin_time = None 
                        seconddegree_checkout_time = None

                        with open(file_path, "r") as csv_file:
                            csv_read = csv.DictReader(csv_file)
                            # arr[0][i]: Get Check in date of infected
                            # arr[2][i]: Get Check in timing of infected 
                            # arr[3][i]: Get Check out timing of infected
                            # arr[4][i]: Get infected person
                            # Reformat check in date as datetime libraray 
                            line_count = 0
                            for row in csv_read:
                                if line_count < 1:
                                    line_count += 1
                                else:
                                    # Get Normal Person's Check in/out information
                                    normal_checkin_date = datetime.datetime.strptime(row["Check-in date"], "%d/%m/%Y")
                                    normal_checkin_time = datetime.datetime.strptime(row["Check-in time"], "%H%M")
                                    normal_checkout_time = datetime.datetime.strptime(row["Check-out time"], "%H%M")
                                    
                                    # Check Condition: Infected person date == Normal person date
                                    if arr[0][i] == normal_checkin_date:
                                        # Check Condition: Normal person time range in within the infected person time range
                                        if (normal_checkout_time < arr[2][i]) or (normal_checkin_time > arr[3][i]):
                                            continue
                                        else:
                                            # Check whether its first degree contact or 2nd degree
                                            # Needs editing here
                                            if flag is True:
                                                newHash.put(normal_checkin_date, row["Phone No."], location, arr[4][i], "Orange")
                                            else:
                                                # Determine the 1st degree person
                                                check_in_value = abs(arr[2][i] - normal_checkin_time)
                                                check_out_value = abs(arr[3][i] - normal_checkout_time)
                                                if check_in_value < check_out_value:
                                                    newHash.put(normal_checkin_date, row["Phone No."], location, arr[4][i] ,"Yellow")
                                                else:
                                                    newHash.put(normal_checkin_date, row["Phone No."], location, arr[5][i] ,"Yellow")

                                            # Logic to get checkindate, general range of 2nd degree contact 
                                            if seconddegree_checkin_date is None:
                                                seconddegree_checkin_date = normal_checkin_date

                                            if seconddegree_checkin_time is None:
                                                seconddegree_checkin_time = normal_checkin_time
                                                firstdegree_phone_number_check_in = row["Phone No."]
                                            elif seconddegree_checkin_date > normal_checkin_date:
                                                seconddegree_checkin_time = normal_checkin_date
                                                firstdegree_phone_number_check_in = row["Phone No."]

                                            if seconddegree_checkout_time is None:
                                                seconddegree_checkout_time = normal_checkout_time
                                                firstdegree_phone_number_check_out = row["Phone No."]
                                            elif seconddegree_checkout_time < normal_checkout_time:
                                                seconddegree_checkout_time = normal_checkout_time
                                                firstdegree_phone_number_check_out = row["Phone No."]

                        # Append second degree contact date and time range to file
                        # Check Condition: True is the non-recursive call
                        if flag is True:
                            second_filename = "SecondDegreeRange_SE.csv"
                            file_exists = os.path.isfile(second_filename)
                            with open("SecondDegreeRange_SE.csv", "a") as csv_file:
                                headers = ['Check-in date', 'Check-in location', 'Check-in time', 'Check-out time', 'Phone Number Check in', 'Phone Number Check Out']
                                data_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                                if not file_exists:
                                    data_writer.writerow(headers)

                                # Reformat Date & Time
                                seconddegree_checkin_date = datetime.date.strftime(seconddegree_checkin_date, "%d/%m/%Y")
                                seconddegree_checkin_time = datetime.datetime.strftime(seconddegree_checkin_time, "%H%M")
                                seconddegree_checkout_time = datetime.datetime.strftime(seconddegree_checkout_time, "%H%M")
                                newList = [seconddegree_checkin_date, location, seconddegree_checkin_time, seconddegree_checkout_time, firstdegree_phone_number_check_in, firstdegree_phone_number_check_out]
                                data_writer.writerow(newList)

                    except Exception as e:
                        print(e)

# Write HashMap to Csv
def writeToCsv(newHash, filename, color):
    with open(filename, mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(newHash.st)):
            newList = list()
            temp = newHash.st[i]
            if temp == None:
                continue
            else:
                while temp is not None:
                    if temp.color == color:
                        newList.append(temp.value)
                    temp = temp.next
                # Get Date of the Hash Map
                newList.insert(0, str(newHash.st[i].key).split(" ")[0])
                data_writer.writerow(newList)

# Write to CSV to be used for HeatMap and Website Table
def CsvForHtml(newHash, infectedperson):
    filename = "WriteToHtml.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, mode='w') as data_file:
        headers = ['Date', 'Phone-Number', 'Location', 'Degree Contact']
        data_writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        if not file_exists:
            data_writer.writerow(headers)
        
        for i in range(len(newHash.st)):
            newList = list()
            temp = newHash.st[i]
            if temp == None:
                continue
            else:
                while temp is not None:
                    if temp.parentNode is infectedperson:
                        data_writer.writerow([str(temp.key).split(' ')[0], temp.value, temp.location, "First Degree"])
                    else:
                        data_writer.writerow([str(temp.key).split(' ')[0], temp.value, temp.location, "Second Degree"])
                    temp = temp.next


#################### Second Degree Contact Code ############################

def SearchSecondDegree():
    arr = selectInfected("SecondDegreeRange", False)
    SearchContacted(None, arr, newHash, False)

def WriteSecondDegreeToCsv(newHash):
    writeToCsv(newHash, "SecondDegree_SE.csv", "Yellow")

def reset():
    os.remove("SecondDegreeRange_SE.csv")


infectedperson = "86148198"
if len(infectedperson) != 8:
    print("Invalid phone number")
else:
    # Step2. Get Check in and Check out from Infected person
    arr = selectInfected(infectedperson, True)
    # Step 3. Search for people who enter mall within the time range of infected person
    SearchContacted(infectedperson, arr, newHash, True)
    # Step 4. Write Result to csv 
    writeToCsv(newHash, infectedperson + "_FirstDegree_SE.csv", "Orange")


## Indirect Contact
SearchSecondDegree()
WriteSecondDegreeToCsv(newHash)
newHash.printHashMap()

CsvForHtml(newHash, infectedperson)

reset()
