from movableEntity import *

class Arrow(MovableEntity):

    def __init__(self,x_position,y_position):
        MovableEntity.__init__(self,x_position,y_position,2,20)
        self.speedX = 3
        self.changeXMov(1)
        self.setMovementFrames([self.frame_1(),self.frame_2()])

    def checkIfReachedLimit(self):
        if self.x_position < 25:
            self.destroy()
        
    def display(self):
        super().display()
        self.checkIfReachedLimit()

    def frame_1(self):
        list_coordinates = [[0,0],[0,5],[20,5],[20,0]]
        return [DrawElement().setDraw([1,1,1],list_coordinates)]

    def frame_2(self):
        list_coordinates = [[0,0],[0,5],[20,5],[20,0]]
        return [DrawElement().setDraw([1,1,1],list_coordinates)]

