from colisionsManager import *

class EnemyDestroyColision(ColisionsManager):

    def manageColision(self, entitieA, entitieB):
        entitieB.destroy()