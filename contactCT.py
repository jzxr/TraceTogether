import datetime as DT
import csv, os
from pathlib import Path
from itertools import chain
from DataStructuresandAlgorithms.AVL import AVL_Tree
from DataStructuresandAlgorithms.SeperateChaining import HashMap

#Create a CSV of first Degree Contact.
def firstDegreeCT(infected_phoneNo, infectionDate, days):
    data = []

    #Read CSV
    root = Path("Data Sets/Contact Tracing/")
    fileName = str(infected_phoneNo) + "_CT.csv"
    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(e)
        return False

    #Get Index of infection date.
    for i in range(25):
        if data[i][0] == infectionDate:
            index = i

    #Get Past x days contacts
    popcount = index - days + 1
    for i in range(0,popcount):
        data.pop(0)
    
    #Create Comfirm Close Contacts
    comfirmList = []
    dateList = []
    for i in range(0,len(data)):
        dateList = []
        dateList.append(data[i][0])

        for r in range(1,len(data[i])):
            string = data[i][r]
            x = string.split(":")

            #if distance less than 5 and contact duration more than 4 mins
            if int(x[1]) <= 2 and int(x[2]) >= 30:
                dateList.append(int(x[0]))
        
        comfirmList.append(dateList)

    #Write to CSV
    root = Path("Data Sets/Results/")
    fileName = str(infected_phoneNo) + "_firstDegreeContact.csv"
    directory = root / fileName
    try:
            writer =csv.writer(open(directory, "w"), delimiter=",", lineterminator = "\n")
            writer.writerows(comfirmList)
    except Exception as e:
        print(e)
        return False

#Create and return a list of first Degree contact with CT data and without.
def secondDegreeCTExist(infected_phoneNo):
    data = []

    #Read CSV file and create 1D list
    root = Path("Data Sets/Results/")
    fileName = str(infected_phoneNo) + "_firstDegreeContact.csv"
    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row.pop(0)
                data.append(row)
    except Exception as e:
        print(e)
        return False
    data = list(chain.from_iterable(data))

    #Check if CT file Exist
    data_CT_True = []
    data_CT_False = []

    root = Path("Data Sets/Contact Tracing/")
    for i in range(0,len(data)):
        fileName = data[i] + "_CT.csv"
        directory = root / fileName
        if os.path.isfile(directory):
            data_CT_True.append(data[i])
        else:
            data_CT_False.append(data[i])
    
    return data_CT_True, data_CT_False

#Create a CSV of second Degree Contact
def secondDegreeCT(infected_phoneNo, infectionDate, data_CT_True):
    for i in range(0,len(data_CT_True)):
        firstDegreeCT(data_CT_True[i], infectionDate, 7)
        #Rename file
        root = Path("Data Sets/Results/")
        fileName = data_CT_True[i] + "_firstDegreeContact.csv"
        src = root / fileName
        fileName = str(infected_phoneNo) + "_" + data_CT_True[i] + "_SecondDegreeContact.csv"
        dst = root / fileName
        os.replace(src, dst)

#Create Second Degree CSV using HashMap
def mergeSecondDegreeCT(infected_phoneNo, data_CT_True):
    newHash = HashMap()
    for i in data_CT_True:
        data = []
        root = Path("Data Sets/Results/")
        fileName = str(infected_phoneNo) + "_" + str(i) + "_SecondDegreeContact.csv"
        directory = root / fileName
        try:
            with open(directory,'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except Exception as e:
            print(e)
        
        for i in range(0,len(data)):
            #print(str(data[i][0]))
            for r in range(1,len(data[i])):
                newHash.put(str(data[i][0]),str(data[i][r]))

    root = Path("Data Sets/Results/")
    fileName = str(infected_phoneNo) + "_secondDegreeContact.csv"
    directory = root / fileName
    newHash.printHashMap()
    newHash.writeToCsv(newHash, directory)

#Create a csv with numbers where TT data needs to be taken from users.
def getTTdata(infected_phoneNo, data_CT_False):
    root = Path("Data Sets/Results/")
    fileName = str(infected_phoneNo) + "_getTTofCT.csv"
    directory = root / fileName
    try:
        writer =csv.writer(open(directory, "w"), delimiter = ",",  lineterminator = "\n")
        writer.writerow(["Missing TT and SE data."])
        for i in data_CT_False:
            writer.writerow([i])
    except Exception as e:
        print(e)

#Format CSV to Ui requriments
def uiFormating(infected_phoneNo, deg):
    data = []
    root = Path("Data Sets/Results/")

    if deg == 1:
        fileName = str(infected_phoneNo) + "_firstDegreeContact.csv"
    elif deg ==2:
        fileName = str(infected_phoneNo) + "_secondDegreeContact.csv"

    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(e)
        return False

    if deg ==1:
        fileName = str(infected_phoneNo) + "_UiFirstDegreeContact.csv"
    elif deg ==2:
        fileName = str(infected_phoneNo) + "_UisecondDegreeContact.csv"


    directory = root / fileName
    #format to Ui requriments.
    try:
        writer =csv.writer(open(directory, "w"), delimiter = ",",  lineterminator = "\n")
        Header = ['Date','Phone No.']
        writer.writerow(Header)
        for i in range(0,len(data)):
            date = data[i][0]
            for r in range(1,len(data[i])):
                temp2 = []
                temp2.append(date)
                temp2.append(data[i][r])
                writer.writerow(temp2)
    except Exception as e:
        print(e)

#Just call this for results of first degree and second degree. 
def contactCT(infected_phoneNo,infectionDate, days):
    firstDegreeCT(infected_phoneNo,infectionDate,days)
    data_CT_True, data_CT_False = secondDegreeCTExist(infected_phoneNo)

    #Remove Duplicated numbers and sort using BST.
    newTree1 = AVL_Tree()
    for i in data_CT_True:
        newTree1.put(str(i))

    data_CT_True = newTree1.inOrder()

    newTree2 = AVL_Tree()
    for i in data_CT_False:
        newTree2.put(str(i))

    data_CT_False = newTree2.inOrder()

    secondDegreeCT(infected_phoneNo, infectionDate, data_CT_True)
    mergeSecondDegreeCT(infected_phoneNo, data_CT_True)
    uiFormating(infected_phoneNo,1)
    uiFormating(infected_phoneNo,2)
    getTTdata(infected_phoneNo,data_CT_False)