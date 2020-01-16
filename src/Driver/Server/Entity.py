import math

class Entity:

    def __init__(self, xPos, yPos, wd, ht):
        self.x = xPos
        self.y = yPos
        self.wd = wd
        self.ht = ht
    
    def distancePT(self, x, y): 
        """Find the distance between an object and a point"""
        return (self.x - x)**2 + (self.y - y)**2
