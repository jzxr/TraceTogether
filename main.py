from contactCT import contactCT
from sms import sendSHN_Notice
from FindContacted_SE import findContactSE
from infectedGraph_SE import infectedPlot
from clusterTable import createClusterTable
#CLI interface

def main():

    datelist = ['01','02','03','04','05','06','07','08','09']
    #Inputs
    infected_phoneNo = input("Please Enter the infected Phone No.: 86148198\n")
    if len(infected_phoneNo) != 8:
        print("Invalid Phone Number")
    else:
        infectionDate = "13/2/2021"
        infectionDate = input("Please Enter the date of infection: Eg. 13/2/2021 or 9/2/2021\n")

        x = infectionDate.split("/",2)
        if x[0] in datelist:
            x1 = x[0].split("0")
            x1 = x1[1]
            if x[1] in datelist:
                x2 = x[1].split("0")
                x2 = x2[1]
            else:
                x2 = x[1]
            infectionDate = x1 + "/" + x2 + "/" + x[2]        

        #Create CSV of close contact and second contact.
        contactCT(infected_phoneNo,infectionDate,14)
        newHashAVL = findContactSE(infected_phoneNo, infectionDate, 14)

        #Create Cluster Table
        createClusterTable()
        
        #Send SHN Notice and infection vector graph.
        sendSHN_Notice(infected_phoneNo)
        infectedPlot(infected_phoneNo, newHashAVL)

if __name__ == "__main__":
    main()