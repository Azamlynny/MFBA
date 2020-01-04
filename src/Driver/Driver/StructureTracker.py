from Structure import * 

class StructureTracker():

    def __init__(self):
        self.structures = []
        self.structures.append(Tower(xPos = 900, yPos = 900, wd = 100, ht = 100, strength = 5, speed = 0, hp = 1000, hpMax = 1000, hpRegen = 0, atk = 50, atkSpeed = 1.0, armor = 5, atkRange = 500, alliance = "b", visionRange = 1000, atkType = "ranged", projWidth = 25))
        
    def drawStructures(self):
        for i in self.structures:
            i.drawStructure()
                
    def runTowerActions(self, Game):
        # return
        for i in self.structures:
            i.lockTarget(Game)
            i.defaultAttack(Game)
