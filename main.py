from contactCT import contactCT
from sms import sendSHN_Notice
#CLI interface

def main():
    infected_phoneNo = input("Please Enter the infected Phone No.: 88888888\n")
    infectionDate = input("Please Enter the date of infection: Eg. 13/2/2021\n")

    contactCT(infected_phoneNo,infectionDate,14)

    sendSHN_Notice()

if __name__ == "__main__":
    main()

