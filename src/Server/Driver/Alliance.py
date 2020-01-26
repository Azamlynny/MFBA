from Util import *
from Structure import * 

class Alliance():
    
    def __init__(self, teamName):
        self.name = teamName
        self.resolution = 25
        self.vision = [[True for i in range(self.resolution)] for j in range(self.resolution)] 
        self.structures = []
        #self.structures.append(Structure(xPos = 6, yPos = 6, strength = 5, speed = 100, hp = 250, hpRegen = 1.5, atk = 10, armor = 3, atkRange = 100, alliance = "a"))
        
    # Server has true sight of the entire map and does not need to update vision
    # def updateVision(self, Game):
    #     scale = 5000 / self.resolution
    #     for y in range (self.resolution):
    #         for x in range (self.resolution):
    #             visionSuccess = False
    #             for p in Game.PT.players:
    #                 if(p.alliance == "a"):
    #                     if(p.visionRange ** 2 > p.distancePT(x * scale, y * scale)):
    #                         self.vision[x][y] = True
    #                         visionSuccess = True
    #                         break
    #             if(visionSuccess):
    #                 continue
    #             for p in Game.ST.structures:
    #                 if(p.alliance == "a"):
    #                     if(p.visionRange ** 2 > p.distancePT(x * scale, y * scale)):
    #                         self.vision[x][y] = True
    #                         visionSuccess = True
    #                         break
    #             if(visionSuccess):
    #                 continue
    #             for p in Game.CT.creep:
    #                 if(p.alliance == "a"):
    #                     if(p.visionRange ** 2 > p.distancePT(x * scale, y * scale)):
    #                         self.vision[x][y] = True
    #                         break
    #                     else:
    #                         self.vision[x][y] = False # Change back to False
                 
    # Server has true sight of the entire map and odes not need to draw vision                         
    # def drawVision(self, Cam):
    #     fill(0,200)
    #     noStroke()
    #     scale = 5000 / self.resolution
    #     for y in range (0,self.resolution):
    #         for x in range (0,self.resolution):
    #             if(self.vision[x][y] == 0): 
    #                 if(sd(Cam, x * scale,y * scale,scale,scale)):
    #                     rect(scale * x, scale * y, scale, scale) 
        
