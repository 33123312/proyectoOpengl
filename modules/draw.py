from turtle import heading, width
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np


#----------Herramientas de dibujo----------------------
def poligon(xc,yc,R,L,C):
    angle = 2*3.141592/L
    #aqui se dibuja
    glBegin(GL_POLYGON) #iniciamos una primitiva, solo puede empezar con una primitiva
    #pueden ser puntos, lineas, grupo conectado de lineas, poligonos,etc
    for i in range(L):
        x = xc + R*np.cos(angle*i)
        y = yc + R*np.sin(angle*i)
        glVertex2d(x,y) #especifica las coordenadas del vertices
    glEnd()#la terminamos


def poligon_coordinates(xc,yc,R,L):
    angle = 2*3.141592/L
    list_coordinates = []
    for i in range(L):
        x = xc + R*np.cos(angle*i)
        y = yc + R*np.sin(angle*i)
        list_coordinates.append([x,y])
    return list_coordinates

def frame_1(R):
    angle = 2*3.141592/32
    list_coordinates = []
    for i in range(32):
        x = R*np.cos(angle*i)
        y = R*np.sin(angle*i)
        list_coordinates.append([x,y])
    return list_coordinates

def frame_2(R):
    angle = 2*3.141592/32
    list_coordinates = []
    list_coordinates.append([0,0])
    for i in range(4,29):
        x = R*np.cos(angle*i)
        y = R*np.sin(angle*i)
        list_coordinates.append([x,y])
    return list_coordinates