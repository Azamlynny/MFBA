class Camera():
    
    def __init__(self, startX, startY):
        self.xshift = startX
        self.yshift = startY 
        self.moveSpeed = 15
        
    def updateCam(self):
        translate(self.xshift, self.yshift)
