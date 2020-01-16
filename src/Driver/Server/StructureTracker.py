from Structure import * 

class StructureTracker():

    def __init__(self):
        self.structures = []
        # Team A
        # Nexus towers
        self.structures.append(Tower(xPos = 500, yPos = 4350, alliance = "a"))
        self.structures.append(Tower(xPos = 650, yPos = 4500, alliance = "a"))
        # Top Lane towers
        self.structures.append(Tower(xPos = 350, yPos = 3500, alliance = "a"))
        self.structures.append(Tower(xPos = 350 , yPos = 1900, alliance = "a"))
        # Bottom Lane towers
        self.structures.append(Tower(xPos = 1500, yPos = 4500, alliance = "a"))
        self.structures.append(Tower(xPos = 3600, yPos = 4500, alliance = "a"))
        # Middle Lane towers
        self.structures.append(Tower(xPos = 1000, yPos = 4000, alliance = "a"))
        self.structures.append(Tower(xPos = 1750, yPos = 3250, alliance = "a"))
        
        # Team B
        # Nexus towers
        self.structures.append(Tower(xPos = 4400, yPos = 600, alliance = "b"))
        self.structures.append(Tower(xPos = 4250, yPos = 450, alliance = "b"))
        # Top Lane towers
        self.structures.append(Tower(xPos = 3700, yPos = 500, alliance = "b"))
        self.structures.append(Tower(xPos = 1700, yPos = 500, alliance = "b"))
        # Bottom Lane towers
        self.structures.append(Tower(xPos = 4500, yPos = 1200, alliance = "b"))
        self.structures.append(Tower(xPos = 4500, yPos = 2700, alliance = "b"))
        # Middle Lane towers
        self.structures.append(Tower(xPos = 3950, yPos = 1000, alliance = "b"))
        self.structures.append(Tower(xPos = 3150, yPos = 1700, alliance = "b"))

    def drawStructures(self, Cam):
        for i in self.structures:
            i.drawStructure(Cam)
                
    def runTowerActions(self, Game):
        # return
        for i in self.structures:
            i.lockTarget(Game)
            i.defaultAttack(Game)
