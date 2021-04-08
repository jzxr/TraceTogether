import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path
from itertools import chain

# Helper Function to adds 1st degree and 2nd degree node to graph
def createNodes_Edge_First(graph, infectedNumber, newHashAVL):
    key_list = list(newHashAVL.key.keys())
    val_list = list(newHashAVL.key.values())
    
    for i in range(len(newHashAVL.st)):
        
        createNodes_Edge_First2(newHashAVL.st[i], graph, infectedNumber)

# Add 1st and 2nd degree node to graph
def createNodes_Edge_First2(node, graph, infectedNumber):
    if node:
        createNodes_Edge_First2(node.left, graph, infectedNumber)

        if node.parentNode is not infectedNumber:
            graph.add_node(node.parentNode)
            graph.add_edge(node.parentNode, node.value)
            graph.add_edge(infectedNumber, node.parentNode)

        createNodes_Edge_First2(node.right, graph, infectedNumber)

# Categories the infected person, 1st and 2nd degree with different colors
# Red: Infected Person
# Orange: 1st Degree Contact
# Yellow: 2nd Degree Contact
def createColorNodes(graph, infectedNumber):
    color_map = []
    for node in graph:
        if node == infectedNumber:
            color_map.append('red')
        elif infectedNumber in nx.all_neighbors(graph, node):
            color_map.append('orange')
        else:
            color_map.append('yellow')
    
    return color_map
        
# Driver Function
def infectedPlot(infectedNumber, newHashAVL):
    graph = nx.Graph()

    createNodes_Edge_First(graph, infectedNumber, newHashAVL)

    graph.add_node(infectedNumber, color= "red")

    color_map = createColorNodes(graph, infectedNumber)
    nx.draw(graph, node_color=color_map, with_labels=False)
    plt.savefig("graph.png", format= "png")
    #plt.show()
