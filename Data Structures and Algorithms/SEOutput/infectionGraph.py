import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path
from itertools import chain
from HashMap import newHash

def createNodes_Edge_First(graph):
    key_list = list(newHash.key.keys())
    val_list = list(newHash.key.values())
    
    for i in range(len(newHash.st)):
        temp = newHash.st[i]
        counter = 0
        while temp is not None:
            graph.add_node(temp.value)
            graph.add_edge(temp.parentNode, temp.value)
            temp = temp.next 
        print()

def createColorNodes(graph, infectedNumber):
    color_map = []
    for node in graph:
        print(node)
        if node == infectedNumber:
            color_map.append('red')
        elif infectedNumber in nx.all_neighbors(graph, node):
            color_map.append('orange')
        else:
            color_map.append('yellow')
    
    return color_map
        

infectedNumber = "86148198"
graph = nx.Graph()

createNodes_Edge_First(graph)

graph.add_node(infectedNumber, color= "red")

color_map = createColorNodes(graph, infectedNumber)
nx.draw(graph, node_color=color_map)
plt.savefig("graph.png", format= "png")
plt.show()
