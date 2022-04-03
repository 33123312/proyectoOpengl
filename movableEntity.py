from entity import *

class MovableEntity(Entity):
    x_limit = 0
    y_limit = 0

    speedX = 0
    speedY = 0


    frame_flag = False 

    MOV_X = 0
    MOV_Y = 0

    def __init__(self,x_position,y_position,w,h) :
        Entity.__init__(self,x_position,y_position,w,h)
        

    def setMovementFrames(self,frames):
        self.movementFrames = frames

    def setXLimit(self,limit):
        self.x_limit = limit

    def setYLimit(self,limit):
        self.y_limit = limit

    def build(self):
        super().build()
        self.timer_pacman_frame(0)
        self.timer_movement(0)
        return self
        
    
    def canInc(self,speed,ori,currentMov):
        newMov = currentMov + ori*speed
        return newMov <= speed and newMov >= -speed


    def changeYMov(self,ori):
        if self.canInc(self.speedY, ori,self.MOV_Y):
            self.MOV_Y =self.MOV_Y + ori*self.speedY


    def changeXMov(self,ori):
        if self.canInc(self.speedX, ori,self.MOV_X):
            self.MOV_X = self.MOV_X + ori*self.speedX


    def timer_pacman_frame(self, value):
        if not self.isDestroyed and not(self.MOV_X == 0 and self.MOV_Y == 0) :
            if self.frame_flag: 
                self.current_frame = self.movementFrames[0]
            else:
                self.current_frame = self.movementFrames[1]

            self.frame_flag = not self.frame_flag
            glutPostRedisplay()
            

        glutTimerFunc(100,self.timer_pacman_frame,5)


    def timer_movement(self,value):
        if not self.isDestroyed:
            self.move()
            glutPostRedisplay()
            glutTimerFunc(10,self.timer_movement,5)

    def move(self):
        newX = self.x_position + self.MOV_X
        newY = self.y_position + self.MOV_Y

        if  self.x_limit > newX + self.w and newX > 0:
            self.setXPos(self.x_position + self.MOV_X)
        if  self.y_limit > newY and newY > 0:
            self.setYPos(self.y_position + self.MOV_Y)

    
        