from Structure import * 

class Alliance():
    
    def __init__(self, teamName):
        self.name = teamName
        self.resolution = 100a
        self.vision = [[0 for i in range(self.resolution)] for j in range(self.resolution)] 
        self.structures = []
        #self.structures.append(Structure(xPos = 6, yPos = 6, strength = 5, speed = 100, hp = 250, hpRegen = 1.5, atk = 10, armor = 3, atkRange = 100, alliance = "a"))
        
    def updateVision(self, Game):
        scale = 10000 / self.resolution
        for y in range (self.resolution):
            for x in range (self.resolution):
                for p in Game.PT.players:
                    if(p.alliance == "a"):
                        if(p.visionRange > p.distancePT(x * scale, y * scale)):
                            self.vision[x][y] = True
                            break
                        else:
                            self.vision[x][y] = False
                    else:
                        break    
                    
    def drawVision(self):
        fill(0,200)
        noStroke()
        scale = 10000 / self.resolution
        for y in range (0,self.resolution):
            for x in range (0,self.resolution):
                if(self.vision[x][y] == 0): 
                    rect(scale * x, scale * y, scale, scale) 
        
