class Alliance():
    
    def __init__(self, teamName):
        self.name = teamName
        self.resolution = 100
        self.vision = [[0 for i in range(self.resolution)] for j in range(self.resolution)] 
        
    def updateVision(self):
        return
    
    def drawVision(self):
        fill(0,200)
        noStroke()
        scale = 10000 / self.resolution
        for y in range (0,self.resolution):
            for x in range (0,self.resolution):
                if(self.vision[x][y] == 0): 
                    rect(scale * x, scale * y, scale, scale) 
        
