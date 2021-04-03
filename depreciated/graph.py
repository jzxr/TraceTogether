class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        # List of adjacent node objects
        self.adj = []

class Graph(object):
    def __init__(self):
        # Adjacency list
        self.nodes = {}

    def add(self, f, t):
        if f not in nodes:
            self.nodes[f] = Node(key=f)
        if t not in nodes:
            self.nodes[t] = Node(key=t)
        if t not in self.nodes[f].adj:
            self.nodes[f].adj.append(self.nodes[t])

# Create graph object
graph = Graph()
# Loop the elements in the row
# ...
for number in range(len(row)):
    if number == 0:
        phone_number = row[number]
    else:
        if row[number] == -1:
            graph.add(phone_number,phonenumbers[number])