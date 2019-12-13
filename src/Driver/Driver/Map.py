class Map():
    
    def __init__(self):
        self.objects = []

    # def loadMap(self):
    #     print("")
        
    def drawMap(self, Team):
        background(0)
        fill(245)
        rect(0,0,10000,10000)
        
        Team.drawVision()
