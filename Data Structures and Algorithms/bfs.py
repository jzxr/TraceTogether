# Time Complexity: 
'''
while loop: at most one time for each node
for loop: at most one for rach edge?
Combining: O(V+E)

Searching:
O(V); V for vertices
'''

from adjacencylist import g
from queue import q

#g.printGraph(g)

def bfs(start):
    # Set Starting Node to Grey, 0 distance and No Prececessor
    start.setColor("Grey")
    start.setDistance(0)
    start.setPrececessor(None)

    # Enqueue starting node to queue
    q.enqueue(start)

    while q.isEmpty() is False:
        currentNode = q.dequeue()
        # For all adjacent Node in currentNode
        for node in currentNode.connectedTo:
            #print("NB:", node.getId(), ", Color", node.getColor())
            if node.getColor() == "White":
                node.setColor("Grey")
                # Current Precessor as Parent Node
                node.setPrececessor(currentNode.getId())
                node.setDistance(currentNode.getDistance() + 1)
                q.enqueue(node)
            currentNode.setColor("Black")

def printContact():
    first_degree = list()
    second_degree = list()
    for vertices in g:
        print(vertices.getId())


bfs(g.getVertex(10))
print()
printContact()
