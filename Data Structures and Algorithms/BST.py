# Normal Binary Tree Complexity 
'''
Worst Case for Search and Insert: O(N)
Average Case for Search and Insert: O(logn)
'''

class Node:
    left = None
    right = None
    # Keep Track of number of node below this node
    count = 0
    # Keep Track on the number of repetition
    counter = 0
    key = 0

    def __init__(self, key):
        self.key = key

class BST:

    def __init__(self):
        self.root = None 

    def get(self, key):
        p = self.root
        while p is not None:
            # If key is more then currentNode, go right
            if key == p.key:
                return p
            elif key > p.key:
                p = p.right
            # If key is less then currentNode, go left 
            else:
                p = p.left
        # Return none if key does not exist
        return None

    def put(self, key):
        self.root = self.put2(self.root, key)

    # If there a need to track the height
    def put2(self, node, key):
        # If there is no root Node, create
        if node is None:
            return Node(key)
        if key > node.key:
            # Why is this here?
            node.right = self.put2(node.right, key)
        elif key < node.key:
            node.left = self.put2(node.left, key)
        else:
            node.counter += 1
        # Why is this here?
        return node

    def inOrder(self):
        return self.inOrder2(self.root)

    def inOrder2(self, node):
        arr = []
        if node:
            arr += self.inOrder2(node.left)
            arr.append(node.key)
            arr += self.inOrder2(node.right)
        return arr

    def preOrder(self):
        return self.preOrder2(self.root)

    def preOrder2(self, node):
        arr = []
        if node:
            arr.append(node.key)
            arr += self.preOrder2(node.left)
            arr += self.preOrder2(node.right)
        return arr

newTree = BST()
newTree.put(5)
newTree.put(7)
newTree.put(1)
newTree.put(2)
newTree.put(10)
newTree.put(8)
print(newTree.get(10).key)
print(newTree.preOrder())
