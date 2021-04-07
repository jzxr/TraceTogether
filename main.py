from contactCT import contactCT
from sms import sendSHN_Notice
from FindContacted_SE import findContactSE
from infectedGraph_SE import infectedPlot
#CLI interface

def main():
    #Inputs
    infected_phoneNo = input("Please Enter the infected Phone No.: 86148198\n")
    if len(infected_phoneNo) != 8:
        print("Invalid Phone Number")
    else:
        infectionDate = "13/2/2021"
        infectionDate = input("Please Enter the date of infection: Eg. 13/2/2021\n")

        #Create CSV of close contact and second contact.
        contactCT(infected_phoneNo,infectionDate,14)
        findContactSE(infected_phoneNo)

        #Send SHN Notice and infection vector graph.
        sendSHN_Notice()
        infectedPlot(infected_phoneNo)

if __name__ == "__main__":
    main()