import numpy as np

def translate(coordinates, x_dist, y_dist):
    #coordenadas es lista bidimencional con valores de x y y
    coord = []
    for coordinate in coordinates:
        coord.append([coordinate[0] + x_dist, coordinate[1] + y_dist])
    return coord

def resize(coordinates, ex, ey):
    #coordenadas es lista bidimencional con valores de x y y
    for i in range(len(coordinates)):
        coordinates[i][0] = int(ex*coordinates[i][0])
        coordinates[i][1] = int(ey*coordinates[i][1])
    return coordinates

def rotate(coordinates, theta):
    #coordenadas es lista bidimencional con valores de x y y
    #theta en radianes
    coord = []
    for i in range(len(coordinates)):
        coord.append([int(np.cos(theta)*coordinates[i][0]+np.sin(theta)*coordinates[i][1]),int(-np.sin(theta)*coordinates[i][0]+np.cos(theta)*coordinates[i][1])])
        #coordinates[i][0] = int(np.cos(theta)*coordinates[i][0]+np.sin(theta)*coordinates[i][1])
        #coordinates[i][1] = int(-np.sin(theta)*coordinates[i][0]+np.cos(theta)*coordinates[i][1])
    return coordinates