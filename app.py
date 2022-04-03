from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from prota import *
from enemy import *
from arrow import *
import numpy as np
from enemyDestroyColision import *
from proyecto import *

def timer_enemy(value):
    global enemyColision 

    def getRandom():
        rndY = int(np.random.random()*480)
        return Enemy(450,rndY)

    newEnemy = getRandom()
    app.addEntity(newEnemy)
    enemyColision.addEntityToB(newEnemy)

    glutTimerFunc(700,timer_enemy,5)


global enemyColision 
enemyColision = EnemyDestroyColision()

app = App()
app.enemyColision = enemyColision
app.addColision(enemyColision)

prota = Prota(250,250)
 
app.addEntity(prota)

timer_enemy(0)
app.start()