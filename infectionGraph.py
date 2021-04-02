import matplotlib.pyplot as plt
import networkx as nx
import csv
from pathlib import Path
from itertools import chain

#Read related CSV for graphing and return as a 1D list.
def readCSV_SE(infectedNumber):
    data = []
    #Get Root Path to folder containing CSV.
    root = Path("Data Sets/HashMapResult/")

    fileName = str(infectedNumber) + "_FirstDegree_SE.csv"
    directory = root / fileName

    try:
        with open(directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row.pop(0)
                data.append(row)

            #Convert 2D List to 1D
            data = list(chain.from_iterable(data))
            return data

    except Exception as e:
        print(e)
        return False

#Create Graph Nodes
def createNodes_Edge_First(graph, infectedNumber, data):
    #Set to 25 cause data has to many...
    for i in range(25):
        graph.add_node(data[i], color="orange" )
        graph.add_edge(infectedNumber, data[i])

    graph.add_edge(data[i], 99999999)

def createColorNodes(graph, infectedNumber):
    color_map = []
    for node in graph:
        if node == infectedNumber:
            color_map.append('red')
        elif node == 99999999:
            color_map.append('yellow')
        else:
            color_map.append('orange')
    
    return color_map
        

infectedNumber = 86148198
firstDegreeData_SE =  readCSV_SE(infectedNumber)
graph = nx.Graph()
graph.add_node(infectedNumber, color= "red")
createNodes_Edge_First(graph, infectedNumber, firstDegreeData_SE)
color_map = createColorNodes(graph, infectedNumber)
nx.draw(graph, node_color=color_map, with_labels=True)
plt.savefig("graph.png", format= "png")
plt.show()
