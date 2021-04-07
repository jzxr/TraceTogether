import datetime

class Node:
    # Key is Date
    key = 0
    # Value is Phone Number
    value = 0
    next = None

    def __init__(self, key, value, location, parentNode, color):
        # key is the date 
        self.key = key
        # value is the phone number 
        self.value = value
        self.left = None
        self.right = None 
        self.height = 1

        self.location = location

        self.parentNode = parentNode
        
        # Red: Infected
        # Yellow: 1st Degree
        # Orange: 2nd Degree 
        self.color = color


class HashMap:
    # Date Range: 20/1/2021 to 13/2/21
    dateRange = list()

    def __init__(self, infectionDate, daterange):
        # Size is 25; cause storing contact tracing for 25 days
        self.size = daterange
        # Flag for Probing of Date
        self.flag = [False for x in range(self.size)]
        # ??? 
        self.key = dict()
        # Array for storing Dates
        self.st = [None for x in range(self.size)]

        self.dateBase = datetime.datetime.strptime(infectionDate, '%d/%m/%Y').date()

        self.collectionofDates()
        # Set keys for HashMap for the 25 days
        self.setKey()

    # Get Date Range: 20/1/2021 to 13/2/21
    def collectionofDates(self):
        for i in range(self.size):
            newDate = self.dateBase - datetime.timedelta(days=i)
            HashMap.dateRange.append(int(newDate.strftime('%d%m%Y')))

    def setKey(self):
        for i in range(len(HashMap.dateRange)):
            counter = 0
            while self.flag[(HashMap.dateRange[i] % self.size) + counter] is True:
                if ((HashMap.dateRange[i] % self.size) + counter) < self.size - 1:
                    counter += 1
                else:
                    counter -= self.size - 1
            self.key[HashMap.dateRange[i]] = (HashMap.dateRange[i] % self.size) + counter
            self.flag[(HashMap.dateRange[i] % self.size) + counter] = True

    # Get HashMap Keys
    def getkeys(self):
        return self.key

    # Get Key of Date
    def getKey(self, date):
        date = int(date.strftime('%d%m%Y'))
        key = self.key.get(date)
        if key is not None:    
            return key
        else:
            print("Key", date ,"does not exist")

    def put(self, key, value, location, parentNode, color):
        k = self.getKey(key)
        if k is not None:
            node = self.st[k]
            self.st[k] = self.put2(self.st[k], key, value, location, parentNode, color)
        else:
            return
    
    def put2(self, node, key, value, location, parentNode, color):
        if node is None:
            return Node(key, value, location, parentNode, color)
        elif value < node.value:
            node.left = self.put2(node.left, key, value, location, parentNode, color)
        elif value > node.value:
            node.right = self.put2(node.right, key, value, location, parentNode, color)
        else:
            return node

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

         # LL Rotation
        if balance > 1 and value < node.left.value:
            return self.rightRotate(node)
        
        # RR Right 
        if balance < -1 and value > node.right.value:
            return self.leftRotate(node)

        # Left Right
        if balance > 1 and value > node.left.value:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        # Right Left 
        if balance < -1 and value < node.right.value:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0 
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y


    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def inOrder(self, node):
        arr = []
        if node:
            arr += self.inOrder(node.left)
            arr.append(node.value)
            arr += self.inOrder(node.right)
        return arr

    def preOrder(self, node):
        if node:
            print(node.key, node.value)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def printAVLTree(self):
        key_list = list(self.key.keys())
        val_list = list(self.key.values())

        for i in range(len(self.st)):
            print(key_list[val_list.index(i)], end=": ")
            if self.st[i] is None:
                print("None")
            else:
                contactedlist = self.inOrder(self.st[i])
                print(contactedlist)


