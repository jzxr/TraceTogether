from DataStructuresandAlgorithms.queue import Queue
from DataStructuresandAlgorithms.AVL import AVL_Tree
import csv
from pathlib import Path
from itertools import chain
try:
    from DataStructuresandAlgorithms.whatsapp import send_whatsapp_msg
except Exception as e:
    print(e)


def avlQueueFirst(infected_phoneNo, deg):
    """
    @Param phone no. and 1st or 2nd degree contact.
    @Return Queue Object.
    """

    #Get TT first or second contact data.
    data1 = []
    root = Path("Data Sets/Results/")
    if deg ==1:
        fileName = str(infected_phoneNo) + "_firstDegreeContact.csv"
    elif deg ==2:
        fileName = str(infected_phoneNo) + "_secondDegreeContact.csv"
    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row.pop(0)
                data1.append(row)
    except Exception as e:
        print(e)
        return False

    #Get SE first or second contact data.
    data2 = []
    root = Path("Data Sets/Results/")
    if deg == 1:
        fileName = str(infected_phoneNo) + "_FirstDegree_SE.csv"
    elif deg == 2:
        fileName = str(infected_phoneNo) + "_SecondDegree_SE.csv"
    directory = root / fileName
    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row.pop(0)
                data2.append(row)
    except Exception as e:
        print(e)
        return False

    #Flatten to 1D List.
    data1 = list(chain.from_iterable(data1))
    data2 = list(chain.from_iterable(data2))

    #Merge and remove duplicates.
    ContactAVL = AVL_Tree()
    for i in data1:
        ContactAVL.put(str(i))
    for i in data2:
        ContactAVL.put(str(i))

    toQueue = ContactAVL.inOrder()

    #Add numbers to Queue
    ContactQueue = Queue()
    for i in toQueue:
        number = "+65" + i
        ContactQueue.enqueue(number)

    return ContactQueue

#Dun use this one cause will really send LOL.
def __sendSMS(firstContactQueue, secondContactQueue):

    msgList = ["Hi you been in contact with an infected person. Please Quratine from today.",
    "Hi you been contact with someone that has close contact with an infected, please monitor your health."]

    try:
        while firstContactQueue.isEmpty() is False:
            #send_whatsapp_msg(firstContactQueue.dequeue(), msgList[0]) #This will send, commented out to prevent spamming strangers whatsapp.
            firstContactQueue.dequeue() #for testing
    except Exception as e:
        print(e)
    
    try:
        while secondContactQueue.isEmpty() is False:
            #send_whatsapp_msg(secondContactQueue.dequeue(), msgList[1]) #This will send, commented out to prevent spamming strangers whatsapp.
            secondContactQueue.dequeue() #for testing
    except Exception as e:
        print(e)

    print("All SHN and Notice Sent.")

def actuallySendSMS(phoneNo):
    phoneList = []
    try:
            send_whatsapp_msg(phoneNo, " For Presentation for Grp 2")
    except Exception as e:
        print(e)


def sendSHN_Notice(infected_phoneNo):
    firstContactQueue = avlQueueFirst(86148198,1)
    secondContactQueue = avlQueueFirst(86148198,2)
    __sendSMS(firstContactQueue,secondContactQueue)
    try:
        actuallySendSMS(ActualSend_No)
    except:
        print("No Actual Phone Number")
