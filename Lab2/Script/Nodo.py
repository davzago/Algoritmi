from Lab2.Script import Time

class Node:
    def __init__(self, nome, lng, lat):
        self.nome = nome
        self.lng = lng
        self.lat = lat
        self.adj = set()

    def addAdj(self, node):
        self.adj.add(node)


class Edge:
    def __init__(self, idE):
        self.times = set()
        self.id = idE

    # d_time: departure time
    # a_time: arrival time
    def addTimes(self, d_time, a_time):
        self.times.add((Time.Time(d_time), Time.Time(a_time)))


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def addNode(self, id, nome, lng, lat):
        if id not in self.nodes:
            self.nodes[id] = Node(nome, lng, lat)

    def addEdgeTimes(self, nodo1, nodo2, idE, d_time, a_time):
        if (nodo1, nodo2) not in self.edges:
            self.edges[(nodo1, nodo2)] = Edge(idE)
            self.nodes[nodo1].addAdj(nodo2)

        self.edges[(nodo1, nodo2)].addTimes(d_time, a_time)



