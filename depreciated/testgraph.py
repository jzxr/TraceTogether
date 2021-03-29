
import networkx as nx
import matplotlib.pyplot as plt

#graph will be based on 20/01/2021

graph = {
    "313 Somerset" : {"99053469" : 27, "98741636" : 27},
    "321 Clementi" : {"82863770" : 4},
    "Aperia Mall" : {"93213933" : 1, "99995219": 50, "98439577": 32, "85991110": 4},
    "Bugis Cube" : {"91700369" : 40, "99995219": 50, "98439577": 32, "85991110": 4},
    "Bugis Plus" : {"93213933" : 24},
    "Balestier Hill Shopping Centre" : {"98173219" : 6},
    "Balestier Plaza" : {"91700369" : 158, "97604430" : 2, "99995219" : 2, "97601182" : 2, "86148198" : 2, "88877112" : 2, "91654703" : 44},
    "Cathay Cineleisure Orchard" : {"91164088" : 11},
    "Capitol Singapore" : {"98114818" : 27, "92561060" : 21},
    "City Square Mall" : {"90175180" : 24, "94459175" : 4, "97604430" : 4,  "88877112" : 1, "95749866" : 1},
    "Duo" : {"94185021" : 3},
    "Far East Plaza" : {"92245161" : 9, "90782389" : 21},
    "Funan" : {"86806044" : 11, "96625428" : 4, "98114818" : 1, "92561060" : 1},
    "Gek Poh Shopping Centre" : {"90782389" : 11},
    "Great World City" : {"94185021" : 27},
    "HDB Hub" : {"98173219" : 4, "87686851" : 5},
    "ION Orchard" : {"83858992" : 19},
    "IMM" : {"97936255" : 6, "98173219" : 6, "90515712" : 6, "88539489" : 11},
    "Jcube" : {"99002814" : 1, "90782389" : 1},
    "Jem" : {"98741632" : 8, "96301245" : 3},
    "Jewel Changi" : {"91806790" : 27},
    "Junction 8" : {"87686851" : 3},
    "Jurong Point" : {"98741631" : 1, "98741632" : 4, "96301245" : 1, "85571447" : 1},
    "Liang Court" : {"82116909" : 1},
    "Lucky Plaza" : {"97936255" : 10, "98173219" : 19},
    "Kallang Wave Mall" : {"96493305" : 40, "87083988" : 10},
    "Millenia Walk" : {"92245161" : 31},
    "Orchard Central" : {"96625428" : 6, "91164088" : 3},
    "Orchard Gateway" : {"99995219" : 31, "99002814" : 5},
    "People's Park Centre" : {"95066161" : 49},
    "People's Park Complex" : {"95066161" : 31},
    "Mustafa Shopping Centre" : {"95066161" : 3, "93861925" : 3, "95939567" : 3, "82204942" : 3},
    "Nex" : {"91654703" : 2},
    "Ngee Ann City" : {"99053469": 5, "99002814" : 5},
    "Northpoint" : {"99053469" : 1, "98741636" : 1, "86148198" : 1, "98439574" : 8, "98439575" : 1},
    "OUE Downtown" : {"94185021" : 31},
    "Paragon" : {"83858992" : 7, "91164088" : 7},
    "Paya Lebar Quarter" : {"89083988" : 4, "99124255" : 5},
    "Pioneer Mall" : {"92245161" : 1, "93993463" : 1},
    "Plaza Singapura" : {"92294434" : 1, "91806792" : 2},
    "PoMo" : {"90515712" : 7, "89083988" : 27, "87083988" : 6, "83858992" : 10},
    "Serangoon Plaza" : {"99124255" : 2},
    "Shaw House and Centre" : {"93861925" : 1},
    "Sim Lim Square" : {"96760458" : 11, "90515712" : 9},
    "Sim Lim Tower" : {"96760458" : 8, "90515712" : 6},
    "SIT@DOVER" : {"93993463" : 1},
    "SIT@NP" : {"96008055" : 10, "91164088" : 10},
    "SIT@NYP" : {"91806792" : 26, "93120759" : 1, "93690508" : 1},
    "SIT@RP" : {"93993463" : 3},
    "SIT@SP" : {"96008055" : 6, "91164088" : 6},
    "SIT@TP" : {"96008055" : 5, "91164088" : 5},
    "Sunshine Plaza" : {"82204942" : 1},
    "Suntec City" : {"83858992" : 40, "96625428" : 31, "86806044" : 11},
    "Square 2" : {"95939567" : 1},
    "Tampines 1" : {"96493305" : 31},
    "Tanglin Mall" : {"96625428" : 10, "88539489" : 8},
    "The Shoppes at Marina Bay Sands" : {"87686851" : 40},
    "The Star Vista" : {"85571447" : 7, "83638020" : 1},
    "Velocity@Novena Square" : {"88539489" : 31},
    "Vivo City" : {"82863770" : 27, "94459175" : 5},
    "Westgate Mall" : {"97936255" : 3,"96493305" : 3, "88539489" : 26, "96760458": 8},
    "Westmall" : {"82863770" : 1, "87309912" : 1, "97601182" : 4, "89652292" : 40, "91806790" : 4},
    "Wheelock Place" : {"87686851" : 3, "95066161" : 7, "94185021" : 49},
    "Zhongshan Mall" : {"91700369": 5, "82863770" : 5, "92294434" : 40, "97601182" : 4, "92245160" : 27, "83638020" : 27},
}

def dijikstra(graph,start,end,visited=[], distance = {}, predecessors = {}):
    if start not in graph:
        raise TypeError ('The root of the shortest path tree cannot be found')
    if end not in graph:
        raise TypeError ('The target of the shortest path tree cannot be found')
    if start == end:
        network = []
        pred = end
        while pred != None:
            network.append(pred)
            pred = predecessors.get(pred,None)
        
        temp = network[0]
        for i in range(1,len(network)):
            temp = network[i] + '--->' + temp
        print('Shortest social network (in arr): ' + str(network))
        print('Network: ' + temp + ",    cost=" + str(distance[end]))
    else:
        if not visited:
            distance[start] = 0
        
        for next in graph[start]:
            if next not in visited:
                newDistance < distance.get(next,float('inf'))
                distance[next] = newDistance
                predecessors[next] = start 
        visited.append(start)

        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distance.get(k,float('inf'))
        x = min(unvisited, key = unvisited.get)
        dijikstra(graph,x,start,visited, distance,predecessors)


dijikstra(graph,'Balestier Plaza', '97604430')