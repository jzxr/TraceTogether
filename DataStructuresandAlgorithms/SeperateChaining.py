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
    m = 7
    st = [None for x in range(0,m)]

    def hashcode(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.m

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
            if self.st[i] is not None:
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
        print(self.st)
        # for i in range(len(self.st)):
        #     temp = self.st[i]
        #     if temp is not None:
        #         print(temp.key, end=':')
        #     while temp is not None:
        #         print(temp.value, end = ",")
        #         temp = temp.next
        #     print()
        

# s = SeperateChainingST()
# s.put("H", "Z")
# s.put("M", "A")
# s.put("QUE", "B")
# s.put("Ysb  ss", "C")
# s.put("ojsb", "D")
# s.put("!kjjkasd", "PO")
# s.put("A", "Q")
# s.put("B", "L")
# s.put("C", "N")
# s.put("D", "W")
# s.put("E", "B")
# s.put("F", "K")
# s.print()
