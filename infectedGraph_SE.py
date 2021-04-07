import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path
from itertools import chain
from FindContacted_SE import newHash

def createNodes_Edge_First(graph, infectedNumber):
    key_list = list(newHash.key.keys())
    val_list = list(newHash.key.values())
    
    for i in range(len(newHash.st)):
        
        createNodes_Edge_First2(newHash.st[i], graph, infectedNumber)

def createNodes_Edge_First2(node, graph, infectedNumber):
    if node:
        createNodes_Edge_First2(node.left, graph, infectedNumber)

        if node.parentNode is not infectedNumber:
            graph.add_node(node.parentNode)
            graph.add_edge(node.parentNode, node.value)
            graph.add_edge(infectedNumber, node.parentNode)

        createNodes_Edge_First2(node.right, graph, infectedNumber)

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
        

def infectedPlot(infectedNumber):
    graph = nx.Graph()

    createNodes_Edge_First(graph, infectedNumber)

    graph.add_node(infectedNumber, color= "red")

    color_map = createColorNodes(graph, infectedNumber)
    nx.draw(graph, node_color=color_map, with_labels=False)
    plt.savefig("graph.png", format= "png")
    #plt.show()