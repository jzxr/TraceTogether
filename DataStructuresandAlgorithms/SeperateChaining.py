# Comment: No need implemenet the enttire linked list

class Node:
    key = 0
    value = 0
    next = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

class SeperateChainingST:
    # Size of SeperateChaining
    m = 5
    st = [None for x in range(0, m)]

    def hashcode(self, key):
        return key % self.m

    def put(self, key, value):
        k = self.hashcode(key)
        node = self.st[k]
        while node is not None:
            # value exist
            if node.value == value:
                return
            node = node.next
        # add key to the front of list
        node = Node(key, value)
        node.next = self.st[k]
        self.st[k] = node 

    # Time Complexity: O(E+V) since need traverse thru entire seperate chaining
    def delete(self, value):
        for i in range(len(self.st)):
            # If head of list
            if self.st[i].value == value:
                print("Deleted", self.st[i].value)
                self.st[i] = self.st[i].next
                return
            # If not head of list
            prev = self.st[i]
            temp = self.st[i].next
            while temp is not None:
                if temp.value == value:
                    prev.next = temp.next 
                    print("Deleted", temp.value)
                    return
                temp = temp.next
                prev = prev.next
        print("Value not found")


    def print(self):
        for i in range(len(self.st)):
            temp = self.st[i]
            while temp is not None:
                print(temp.value, end = ",")
                temp = temp.next
            print()

s = SeperateChainingST()
s.put(0, "Z")
s.put(1, "A")
s.put(2, "B")
s.put(3, "C")
s.put(3, "D")
s.put(4, "E")
s.put(4, "F")
s.put(4, "G")
s.put(21, "P")
s.delete("Z")
s.print()
