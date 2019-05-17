from Lab4.Script import Parser
from Lab4.Script import Contea
import pprint
import math

class Cluster:
    def __init__(self, points):
        self.points = points

    def put(self, point):
        self.points.add(point)

def h_clustering(P, k):
    n = len(P)
    sortedP = sorted(P, key=lambda c: c.x) # sortedP = P ordinato secondo la coordinata x
    S = [i for i in range(0, len(P))]
    S.sort(key=lambda i: P[i].y)  # S = lista degli indici i di P ordinati per coordinata y di P[i]

    clusters = set(Cluster([p]) for p in P)

    while len(clusters) > k:
        i, j = fast_closest_pair(clusters, S)
        cluster_i = Cluster(clusters
        clusters.add(Cluster(Cluster))
    

"""
    clusters = set(tuple([p]) for p in P)
    pprint.pprint(clusters)
    while len(clusters) > k:
        i, j = fast_closest_pair(
        clusters.add(tuple([P[i], P[j]]))
        try:
            clusters.remove(tuple([P[i]]))
            clusters.remove(tuple([P[j]]))
        except KeyError:
            return clusters
    return clusters
"""

def slow_closest_pair(P):
    d, i, j = float("inf"), -1, -1
    for u in range(0, len(P)-1):
        for v in range(u + 1, len(P)-1):
            new_d = euclidean_dist(P[u], P[v])
            if new_d < d:
                d = new_d
                i = u
                j = v
    return d, i, j


def split(S, Pl):
    Sl = []
    Sr = []
    for i in range(0, len(S) - 1):
        if S[i] in Pl:
            Sl.append(S[i])
        else:
            Sr.append(S[i])
    return Sl, Sr

def fast_closest_pair(P, S):
    n = len(P)

    if n <= 3:
        return slow_closest_pair(P)

    m = n/2
    Pl = [P[i] for i in range(0, m-1)]
    Pr = [P[i] for i in range(m, n-1)]

    Sl, Sr = split(S, Pl)
    d, i, j = min(fast_closest_pair(Pl, Sl), fast_closest_pair(Pr, Sr))
    mid = 0.5*(P[m-1].x + P[m].x)
    d2, i2, j2 = closest_pair_strip(S, mid, d)
    if d2 < d:
        return d2, i2, j2
    return d, i, j


def closest_pair_strip(P, S, mid, d):
    S1 = []
    for i in range(0, len(S)):
        if abs(P[S[i]].x - mid) < d:
            S1.append(S[i])
    d, i, j = float('inf'), -1, -1
    for u in range(0, len(S) - 2):
        for v in range(u + 1, min(u + 5, len(S) - 1)):
            new_d = euclidean_dist(P[S1[u]], P[S1[v]])
            if new_d < d:
                d = new_d
                i = u
                j = v
    return d, i, j





def euclidean_dist(c1, c2):
    return math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)

L = Parser.Parser()


C = h_clustering(list(set.union(*(l for l in L))), 0)

pprint.pprint(C)