from modules.textures import loadTexture

class DrawElement:

    def setTexture(self,file):
        self.type = "sprite"
        self.texture = loadTexture(file)
        return self

    def setDraw(self,color,coord):
        self.type = "draw"
        self.color = color
        self.coord = coord
        return self

        