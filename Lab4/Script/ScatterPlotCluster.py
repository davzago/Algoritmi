import matplotlib.pyplot as plt
import numpy as np
import math

def scatter_plot_cluster(clusters, P):
    labels = [None for p in P]
    count = 0
    size = 10000
    for i in clusters:
        for j in range(0, len(P)):
            if P[j] in clusters[i]:
                labels[j] = count
        count += 1

    X = np.array([[i.x, i.y, math.ceil(i.population/size)] for i in P])

    img = plt.imread("../File vari/USA_Counties.png")

    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.scatter(X[:,0],X[:,1], s=X[:,2], c=labels, cmap='Paired', alpha=0.5, edgecolors='black')

    plt.savefig("usa_", dpi=1200)
