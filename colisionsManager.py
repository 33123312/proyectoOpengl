
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.transform import *

class ColisionsManager:

    entitiesGroupA = []
    entitiesGroupB = []

    def __init__(self) -> None:
        pass

    def check(self):
        for entityA in self.entitiesGroupA:
            for entityB in self.entitiesGroupB:
                self.checkEntitiesColision(entityA,entityB)
            

    def addEntityTo(self,entity,group):
        group.append(entity)
        def removeEntity():
            group.remove(entity)
        entity.addOnDestroyEvent(removeEntity)
    

    def addEntityToA(self,entity):
        self.addEntityTo(entity,self.entitiesGroupA)


    def addEntityToB(self,entity):
        self.addEntityTo(entity,self.entitiesGroupB)


    def pointIsBetween(self,point,pointInit,pointEnd):
        return point >= pointInit and point <= pointEnd


    def hasColisionInX(self,entitieA,entitieB):
        return self.pointIsBetween(entitieA.x_position,entitieB.x_position,entitieB.entityXend) or self.pointIsBetween(entitieA.entityXend,entitieB.x_position,entitieB.entityXend)


    def hasColisionInY(self,entitieA,entitieB):
        return self.pointIsBetween(entitieA.y_position,entitieB.y_position,entitieB.entityYend) or self.pointIsBetween(entitieA.entityYend,entitieB.y_position,entitieB.entityYend)


    def checkEntitiesColision(self,entitieA,entitieB):
        coincidencInX = self.hasColisionInX(entitieA,entitieB)
        if(coincidencInX):
            coincidencInY = self.hasColisionInY(entitieA,entitieB)
            if(coincidencInY):
                self.manageColision(entitieA,entitieB)

    def manageColision(self,entitieA,entitieB):
        print("colision")