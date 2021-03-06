import math


def calc_center(points):
    x, y = 0, 0

    for p in points:
        x += p.x
        y += p.y

    n = len(points)

    return x/n, y/n


def euclidean_dist(c1, c2):
    return math.sqrt(math.pow(c1[0] - c2[0], 2) + math.pow(c1[1] - c2[1], 2))

def distortion(clusters):
    sum = 0
    for c in clusters:
        for val in clusters[c]:
            sum += math.pow(euclidean_dist((c[0], c[1]), (val.x, val.y)), 2) * val.population
    return sum

