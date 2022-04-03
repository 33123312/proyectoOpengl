from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class App:

    def __init__(self):
        self.main()

    entities = []
    colisionManagers = []

    w,h= 500,500


    def reshape(self, width, height):
        glViewport ( 0, 0, width, height )
        glMatrixMode ( GL_PROJECTION )
        glLoadIdentity()
        glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
        self.w = width
        self.h = height
        glMatrixMode ( GL_MODELVIEW )
        glLoadIdentity()

    def display(self):
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode ( GL_MODELVIEW )
        glLoadIdentity()
        for entity in self.entities:
            entity.display()
            glColor3f(1,1,1)

        for manager in self.colisionManagers:
            manager.check()

        glutSwapBuffers()


    def main(self):
        global w, h, radius, pacman_frame_1, pacman_frame_2

        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize (self.w,self.h)
        glutInitWindowPosition( 0, 0 )

        glutCreateWindow( "Ventana de PyOpenGL" )
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)

        glClearColor(0,0.5,0.25,0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def addEntity(self,entity):
        entity.setApp(self)
        entity.setXLimit(self.w)
        entity.setYLimit(self.h)
        def removeEntity():
            self.entities.remove(entity)
        entity.addOnDestroyEvent(removeEntity)
        entity.build()
        self.entities.append(entity)

    def addColision(self,manager):
        self.colisionManagers.append(manager)
        
    def start(self):
        glutMainLoop()






