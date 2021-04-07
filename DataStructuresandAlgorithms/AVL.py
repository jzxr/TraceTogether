import math

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 
        self.height = 1

class AVL_Tree:
    root = None

    def put(self, key):
        self.root = self.put2(self.root, key)

    def put2(self, node, key):
        # Step 1 - Perfrom normal BST
        # If root is empty
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self.put2(node.left, key)
        else:
            node.right = self.put2(node.right, key)
        
        # Step 2 - Update the hight of the ancestor node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)
        
        # LL Rotation
        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)
        
        # RR Right 
        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        # Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        # Right Left 
        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

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

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def inOrder(self):
        return self.inOrder2(self.root)

    def inOrder2(self, node):
        arr = []
        if node:
            arr += self.inOrder2(node.left)
            arr.append(node.key)
            arr += self.inOrder2(node.right)
        return arr

    def preOrder(self, node):
        if node:
            print(node.key, node)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.key, node)

    # Get Balance 
    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

        