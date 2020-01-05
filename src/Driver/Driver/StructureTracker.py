from Structure import * 

class StructureTracker():

    def __init__(self):
        self.structures = []
        #nexus
        self.structures.append(Tower(xPos = 300, yPos = 4650, alliance = "a"))
        self.structures.append(Tower(xPos = 500, yPos = 4750, alliance = "a"))
        #top
        self.structures.append(Tower(xPos = 350, yPos = 3500, alliance = "a"))
        self.structures.append(Tower(xPos = 350 , yPos = 1900, alliance = "a"))
        #bot
        self.structures.append(Tower(xPos = 1500, yPos = 4500, alliance = "a"))
        self.structures.append(Tower(xPos = 3600, yPos = 4500, alliance = "a"))
        #mid
        self.structures.append(Tower(xPos = 1000, yPos = 4000, alliance = "a"))
        self.structures.append(Tower(xPos = 2000, yPos = 3000, alliance = "a"))
        
        #nexus
        self.structures.append(Tower(xPos = 4700, yPos = 500, alliance = "b"))
        self.structures.append(Tower(xPos = 4450, yPos = 250, alliance = "b"))
        #top
        self.structures.append(Tower(xPos = 3700, yPos = 500, alliance = "b"))
        self.structures.append(Tower(xPos = 1700, yPos = 500, alliance = "b"))
        #bot
        self.structures.append(Tower(xPos = 4500, yPos = 1200, alliance = "b"))
        self.structures.append(Tower(xPos = 4500, yPos = 3200, alliance = "b"))
        #mid
        self.structures.append(Tower(xPos = 3900, yPos = 1000, alliance = "b"))
        self.structures.append(Tower(xPos = 2900, yPos = 2000, alliance = "b"))




        
    def drawStructures(self):
        for i in self.structures:
            i.drawStructure()
                
    def runTowerActions(self, Game):
        # return
        for i in self.structures:
            i.lockTarget(Game)
            i.defaultAttack(Game)
