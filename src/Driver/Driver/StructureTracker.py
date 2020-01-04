from Structure import * 

class StructureTracker():

    def __init__(self):
        self.structures = []
        self.structures.append(Tower(xPos = 900, yPos = 900, alliance = "b"))
        
    def drawStructures(self):
        for i in self.structures:
            i.drawStructure()
                
    def runTowerActions(self, Game):
        # return
        for i in self.structures:
            i.lockTarget(Game)
            i.defaultAttack(Game)
