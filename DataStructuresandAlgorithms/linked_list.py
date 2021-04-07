class LocationNode:
    def __init__(self, location, longtitute, latitute):
        self.location = location 
        self.longtitute = longtitute
        self.latitute = latitute
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, location, longtitute, latitute):
        node = LocationNode(location, longtitute, latitute)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head 
            self.head = node

    def search(self, location):
        temp = self.head 
        while temp is not None:
            if temp.location == location:
                return temp
            temp = temp.next
        print("Location Not Found")

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.location, temp.longtitute, temp.latitute)
                temp = temp.next



     
