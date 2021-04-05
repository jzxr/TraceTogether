class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        # Color to keep track of Visited Node 
        # White: Not Invited 
        # Grey: Partially Visited
        # Black: Fully Visited 
        self.color = None
        # Number of nodes from the origin node
        self.distance = None
        # Parent Node
        self.predecessor = None

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # Replace print Object with the return value
    # def __str__(self):
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPrececessor(self):
        return self.predecessor

    def setPrececessor(self, predecessor):
        self.predecessor = predecessor

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        # Set Vertex color to White
        newVertex.setColor("White")
        return newVertex

    def getVertex(self, n):
        return self.vertList[n]

    def getVertexNB(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def printGraph(self, g):
        for v in g:
            print("Id:", v.getId(), end=" NB: ")
            for w in v.getConnections():
                print(w.getId(), end= " ")
            print()

g = Graph()

g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)
g.addVertex(11)
g.addVertex(12)
g.addVertex(13)
g.addVertex(14)

g.addEdge(1, 5)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 1)
g.addEdge(2, 5)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 6)
g.addEdge(4, 5)
g.addEdge(4, 3)
g.addEdge(4, 9)
g.addEdge(4, 10)
g.addEdge(4, 7)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(5, 4)
g.addEdge(6, 3)
g.addEdge(6, 8)
g.addEdge(7, 4)
g.addEdge(7, 10)
g.addEdge(7, 8)
g.addEdge(8, 7)
g.addEdge(8, 6)
g.addEdge(8, 11)
g.addEdge(9, 4)
g.addEdge(9, 14)
g.addEdge(9, 10)
g.addEdge(10, 9)
g.addEdge(10, 4)
g.addEdge(10, 7)
g.addEdge(10, 12)
g.addEdge(10, 11)
g.addEdge(11, 8)
g.addEdge(11, 10)
g.addEdge(11, 13)
g.addEdge(12, 14)
g.addEdge(12, 13)
g.addEdge(12, 10)
g.addEdge(13, 12)
g.addEdge(13, 11)
g.addEdge(14, 9)
g.addEdge(14, 12)
