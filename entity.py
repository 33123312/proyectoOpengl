from re import A
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.transform import *
from drawElement import *

class Entity:
    isDestroyed = False

    x_position = 0
    y_position = 0

    entityXend = 0
    entityYend = 0

    current_frame = None
    onDestroyEvnts = None

    w = None
    h = None

    center = None
    drawCenter = None

    app = None

    defaultFrame = None

    def __init__(self,x_position,y_position,w,h) :

        self.center = []

        self.draw = []

        self.current_frame = []

        self.onDestroyEvnts = []

        self.w = w
        self.h = h

        self.setXPos(x_position)
        self.setYPos(y_position)

        self.center = [int(w/2),int(h/2)] 

        
    def setApp(self,app):
        self.app = app

    def setDraw (self,frame):
        self.current_frame = frame

    def useDefaultDraw(self):
        self.setDraw(self.defaultFrame)

    def setDefaultdraw(self,frame):
        self.defaultFrame = frame
        self.useDefaultDraw()
        

    def build (self):
        return self


    def display(self):
        for trazo in self.current_frame:
            if trazo.type == "draw":
                glBegin(GL_POLYGON)
                self.drawByhand(trazo)
            else:
                self.drawBySprite(trazo)


    def drawBySprite(self,trazo):
        glEnable(GL_TEXTURE_2D)
        pin_x_start, pin_x_end = (1,0)
        glBindTexture(GL_TEXTURE_2D, trazo.texture)
        glBegin(GL_POLYGON)
        glTexCoord2f(pin_x_start,0)
        glVertex2d(self.x_position,self.y_position)
        glTexCoord2f(pin_x_end,0)
        glVertex2d(self.entityXend,self.y_position)
        glTexCoord2f(pin_x_end,1)
        glVertex2d(self.entityXend,self.entityYend)
        glTexCoord2f(pin_x_start,1)
        glVertex2d(self.x_position,self.entityYend)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def drawByhand(self,trazo):
        color = trazo.color
        cordenadas = trazo.coord
        glColor3f(color[0],color[1],color[2])
        for cor in cordenadas:
            glVertex2d(cor[0] + self.x_position , cor[1] + self.y_position)

        glEnd()

    def setXPos(self,newX):
        self.x_position = newX
        self.entityXend = newX + self.w

    def setYPos(self,newX):
        self.y_position = newX
        self.entityYend = newX + self.h

    def addOnDestroyEvent(self,evnt):
        self.onDestroyEvnts.append(evnt)

    def executeDestroyEvents(self):
        for evnt in self.onDestroyEvnts:
            evnt()

    def destroy(self):
        self.executeDestroyEvents()
        self.isDestroyed = True