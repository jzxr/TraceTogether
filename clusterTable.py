import csv
from pathlib import Path
from DataStructuresandAlgorithms.stack import Stack

#Location Asbtract data type to keep track of location first and second degree count.
class LocationADT():
    #Dictonary to store LocationName:Obj
    LocationDict = {}

    #Add location and Increment contact type.
    def put(self, locationData):
        if locationData[0] in self.LocationDict:
            self.getObj(locationData)
        else:
            self.createObj(locationData)

    #Fetch Object and increment based on contact type.   
    def getObj(self, locationData):
        #Access Dict Object
        temp = self.LocationDict[locationData[0]]
        #Increment Contact Type.
        temp.increase(locationData[1])

    #Create Object for location and increment based on contact type.
    def createObj(self, locationData):
        #Create key with object
        self.LocationDict[locationData[0]] = LocationADTNode()
        #Access Dict Object
        temp = self.LocationDict[locationData[0]]
        #Increment Contact Type.
        temp.increase(locationData[1])

    def getObjDict(self):
        return self.LocationDict

#Location ADT Node.      
class LocationADTNode():
    
    firstDeg = 0
    secondDeg = 0

    def increase(self, ContactType):
        if ContactType == "First Degree":
            self.firstDeg += 1
        elif ContactType == "Second Degree":
            self.secondDeg += 1

    def getData(self):
        return self.firstDeg, self.secondDeg
    

def createClusterTable():

    #Using Stack to make sure all location are accounted for and contact type.
    locationStack = Stack()

    #Abstract Data Type for Location contact type count tracking
    locationAbstract = LocationADT()

    #Read WriteToHtml.csv
    root = Path("Data Sets/Results/")
    fileName = "WriteToHtml.csv"
    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row.pop(0)
                row.pop(0)
                locationStack.push(row)
    except Exception as e:
        print(e)

    #Writer to Cluster Table
    root = Path("Data Sets/Results/")
    fileName = "ClusterTable.csv"
    directory = root / fileName
    try:
        writer = csv.writer(open(directory, "w"), delimiter = ",",  lineterminator = "\n")
        writer.writerow(["Location Name:", "First Degree Count.", "Second Degree Count."])
    except Exception as e:
        print(e)

    while locationStack.isEmpty() is False:
        locationAbstract.put(locationStack.pop())

    tempDict = locationAbstract.getObjDict()
    for i in tempDict:
        tempObj = tempDict[i]
        firstDeg , secondDeg = tempObj.getData()
        writer.writerow([i,firstDeg,secondDeg])