import random
import itertools

from Lab1.Script import Graph


def er_undirected(nodes, probability):
    g = Graph.Graph(nodes)
    if probability > 1:
        probability = 1
    elif probability <= 0:
        return g
    for i in itertools.combinations(range(1, nodes), 2): # crea tutte le combinazioni di lunghezza 2 senza ripetizioni (es: combinations('1234', 2) --> 12 13 14 23 24 34)
        a = random.uniform(0, 1)
        if a < probability:
            g.addArc(i[0], i[1])
    return g


# con n = 6474 e p = 0.0006 viene un numero di archi simile a quello di as20000012.txt


