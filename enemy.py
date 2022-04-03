from movableEntity import *

class Enemy(MovableEntity):

    def __init__(self,x_position,y_position):
        MovableEntity.__init__(self,x_position,y_position,30,30)
        self.speedX = 1
        self.changeXMov(-1)
        self.setMovementFrames([self.frame_1(),self.frame_2()])

    def checkIfReachedLimit(self):
        if self.x_position < 25:
            self.destroy()
        
    def display(self):
        super().display()
        self.checkIfReachedLimit()

    def frame_1(self):
        return [DrawElement().setTexture("Resources/Goomba1.png")]

    def frame_2(self):
        return [DrawElement().setTexture("Resources/Goomba2.png")]

