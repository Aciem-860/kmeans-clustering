import numpy as np
import random as rd
import matplotlib.pyplot as plt

def kmeans(k, points, repetition):
    """
    k          : nombre de clusters (entier > 0)
    points     : tableau de points à n dimensions
    repetition : nombre de recalcul de centroïde
    """
    # initialisation
    init_indices = []
    while len(init_indices) < k:
        index = rd.randint(0, len(points)-1)
        if index not in init_indices:
            init_indices.append(index)

    centroids = []
    for j in init_indices:
        centroids.append(points[j])

    # assignation des points à un centroïde
    clusters = [[] for _ in range(k)]
    
    for x in points:
        index = closest_point(x, centroids)
        clusters[index].append(x)

    #############################################################################################
    #  Puis on calcule pour chaque cluster la moyenne des points, ce sera le nouveau centroïde  #
    #  On fait cela autant de fois que désiré                                                   #
    #############################################################################################
    
    for i in range(repetition):
        centroids = []
        for c in clusters:
            m = []
            m = [0 for _ in range(len(points[0]))] # i-ème élément de m : moyenne de la i-ème coordonnée
                                                   # des pts du cluster
            for x in c:
                for j in range(len(x)):
                    m[j] = x[j]

            for j in range(len(m)):
                m[j] /= len(points)
            centroids.append(m)

        clusters = [[] for _ in range(k)]
        
        for x in points:
            index = closest_point(x, centroids)
            clusters[index].append(x)

    i = 0
    COLOR = ['blue', 'red', 'green']
    for c in clusters:
        x, y = [], []
        for p in c:
            x.append(p[0])
            y.append(p[1])
        plt.scatter(x,y , color = COLOR[i])
        i += 1
    plt.show()
        

def mean(points):
    """
    Renvoie la moyenne des points
    """

    means = []

def closest_point(x, centroids):
    """
    Trouve le centroïde le plus proche de x parmi c
    """
    distances = [] # tableau des distances
    for c in centroids:
        distances.append(distance2(x, c))

    return distances.index(min(distances)) # numéro du cluster auquel appartient x

def distance2(x, y):
    """
    Renvoie la distance euclidienne élevée au carré entre x et y
    x, y : tableaux à n-éléments (dimension n)    
    """
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i])**2
    return d

points = [[0,0], [1,1], [100,0], [100, 2], [20, 15], [21,17]]
x, y = [], []

for p in points:
    x.append(p[0])
    y.append(p[1])

kmeans(3, [[0,0], [1,5], [1010,0], [1000, 2], [20, 15], [21,17], [18,15]], 100)