
from movableEntity import *

class ManejableEntity(MovableEntity):

    def __init__(self, x_position, y_position, w, h):
        MovableEntity.__init__(self,x_position, y_position, w, h)
        self.speedX = 5
        self.speedY = 5
        glutKeyboardFunc(self.keyPressed)
        glutKeyboardUpFunc(self.keyUp)

    def build(self):
        super().build()
        glutKeyboardFunc(self.keyPressed)
        glutKeyboardUpFunc(self.keyUp)
        return self

    def moveTo(self,key,orientation):
        if key == b'w':
            return self.changeYMov(1*orientation)
        if key == b's':
            return self.changeYMov(-1*orientation)
        if key == b'a':
            return self.changeXMov(-1*orientation)
        if key == b'd':
            return self.changeXMov(1*orientation)

    def keyPressed (self, key, x, y):
        return self.moveTo(key,1)

    def keyUp(self ,key,x,y):
        self.useDefaultDraw()
        return self.moveTo(key,-1)

    


    