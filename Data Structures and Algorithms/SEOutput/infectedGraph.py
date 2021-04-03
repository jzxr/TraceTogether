import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path
from itertools import chain
from SecondDegree import newHash

def createNodes_Edge_First(graph, infectedNumber):
    key_list = list(newHash.key.keys())
    val_list = list(newHash.key.values())
    
    for i in range(len(newHash.st)):
        temp = newHash.st[i]
        counter = 0

        while temp is not None:
            if temp.parentNode is not infectedNumber:
                graph.add_node(temp.value)
                graph.add_node(temp.parentNode)
                graph.add_edge(temp.parentNode, temp.value)
                graph.add_edge(infectedNumber, temp.parentNode)
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

createNodes_Edge_First(graph, infectedNumber)

graph.add_node(infectedNumber, color= "red")

color_map = createColorNodes(graph, infectedNumber)
nx.draw(graph, node_color=color_map, with_labels=True)
plt.savefig("graph.png", format= "png")
plt.show()
