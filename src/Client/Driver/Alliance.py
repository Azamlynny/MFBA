from Util import *
from Structure import * 

class Alliance():
    
    def __init__(self, teamName):
        self.name = teamName
        self.resolution = 25
        self.vision = [[False for i in range(self.resolution)] for j in range(self.resolution)] 
        self.structures = []
        
    def updateVision(self, Game):
        """Updates array of entities in your alliance's shared vision"""
        scale = 5000 / self.resolution
        for y in range (self.resolution):
            for x in range (self.resolution):
                visionSuccess = False
                for p in Game.PT.players:
                    if(p.alliance == self.name):
                        if(p.visionRange ** 2 > p.distancePT(x * scale, y * scale)):
                            self.vision[x][y] = True
                            visionSuccess = True
                            break
                if(visionSuccess):
                    continue
                for p in Game.ST.structures:
                    if(p.alliance == self.name):
                        if(p.visionRange ** 2 > p.distancePT(x * scale, y * scale)):
                            self.vision[x][y] = True
                            visionSuccess = True
                            break
                if(visionSuccess):
                    continue
                for p in range(0,len(Game.CT.creepx)):
                    if(Game.CT.creepAlliance[p] == self.name):
                        distance = (Game.CT.creepx[p] - x * scale)**2 + (Game.CT.creepy[p] - y * scale)**2
                        if(500 ** 2 > distance):
                            self.vision[x][y] = True
                            visionSuccess = True
                            break
                if(visionSuccess):
                    continue
                
                # If none of the players, structures, or creep provide vision then set the vision tile to False                
                self.vision[x][y] = False # Change back to False
                       
    def drawVision(self, Cam):
        """Draw fog over where your alliance doesn't have vision"""
        fill(0,200)
        noStroke()
        scale = 5000 / self.resolution
        for y in range (0,self.resolution):
            for x in range (0,self.resolution):
                if(self.vision[x][y] == 0): 
                    if(sd(Cam, x * scale,y * scale,scale,scale)):
                        rect(scale * x, scale * y, scale, scale) 
        
