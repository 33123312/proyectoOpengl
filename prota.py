from enemy import *
import numpy as np
from arrow import *

from manejableEntity import *
from drawElement import *

class Prota(ManejableEntity):

    def __init__(self, x_position, y_position):
        ManejableEntity.__init__(self,x_position, y_position, 20, 30 )
        self.setMovementFrames([self.frame_1(),self.frame_2()])
        self.setDefaultdraw(self.frame_1())

    def keyPressed(self, key, x, y):
        super().keyPressed(key, x, y)
        if key == b'c':
            self.creatArrow()

    def creatArrow(self):
        newArrow = Arrow(self.x_position + 10,self.y_position + 20)
        self.app.addEntity(newArrow)
        self.app.enemyColision.addEntityToA(newArrow)


    def createHead(self):
        angle = 2*3.141592/15
        list_coordinates = []
        for i in range(32):
            x = 10*np.cos(angle*i) + 10
            y = 10*np.sin(angle*i)+ 30
            list_coordinates.append([x,y])

        return DrawElement().setDraw([1,0.8,0.7],list_coordinates)

    def createBody(self):
        list_coordinates = [[0,0],[0,20],[20,20],[20,0]]


        return DrawElement().setDraw([0.8,0.2,0.2],list_coordinates)

    def frame_1(self):

        return [self.createBody(),self.createHead()]


    def frame_2(self):
            
        return [self.createHead(),self.createBody()]



    