class Camera():
    
    def __init__(self, startX, startY):
        self.xshift = startX
        self.yshift = startY 
        self.moveSpeed = 25
        self.drawRings = False
        
    def updateCam(self):
        """Move camera by (xshift, yshift)"""
        translate(self.xshift, self.yshift)
