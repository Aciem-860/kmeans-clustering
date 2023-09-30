import random
import os

def kmeans(k, points, repetition):
    """
    k          : nombre de clusters (entier > 0)
    points     : tableau de points à n dimensions
    repetition : nombre de recalcul de centroïde
    """
    # initialisation
    init_indices = []
    while len(init_indices) < k:
        index = random.randint(0, len(points)-1)
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
    
    for _ in range(repetition):
        ### AFFICHAGE AVANCEE ###
        os.system("cls")
        quantity = int(_ * 20/repetition)
        prog = "#" * quantity
        mprog = "-" * (20 - quantity)
        print("Progression : {}{} * {}% ({}/{})".format(prog, mprog, int(_*100/repetition), _, repetition))
        #########################

        centroids = []
        nb_coordinates = len(points[0])
        for c in clusters:
            mean = []
            for i in range(nb_coordinates):
                s = 0
                for l in c:
                    s += l[i]
                mean.append(s/len(c))
            centroids.append(mean)

        clusters = [[] for _ in range(k)]
        
        for x in points:
            index = closest_point(x, centroids)
            clusters[index].append(x)
        
    # on bricole un peu pour avoir un beau message "100%"
    os.system("cls")
    print("Progression : #################### * 100% ({}/{})".format(repetition, repetition))
    # on retourne les clusters
    return clusters


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