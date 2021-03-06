from Creep import * 
from Util import *

class CreepTracker():

    def __init__(self):
        self.creep = []
                  
    def drawCreep(self, Cam, Alliance):
        """Draw all creeps in vision and their healths"""
        scale = 5000 / Alliance.resolution
        for i in self.creep:
            if(sd(Cam,i.x,i.y,i.wd,i.ht)):
                if(Alliance.vision[int(i.x / scale)][int(i.y / scale)]):
                    if any(j.debuff == "dead" for j in i.debuffs):
                        pass
                    else:
                        i.drawCreep()
                        i.drawHealth()
                
    def runCreepActions(self, Game, Map, GUI):
        """Run all creep-related actions"""
        for i in self.creep:
            if(i.hp <= 0):
                if(GUI.type == "creep"):
                    GUI.playerSlot = 0
                    GUI.type = "player" # Reset GUI to player if it dies
                self.creep.remove(i) # Remove the creep if it dies
            i.runAI(Game, Map)
    
    def spawnCreep(self):
        """Generate creep waves"""
        # Top Lane
        # Team A 
        self.creep.append(Creep(xPos = 340, yPos = 3601, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 300, yPos = 3701, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 370, yPos = 3701, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 340, yPos = 3701, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 340, yPos = 3801, wd = 40, ht = 40, atkRange = 250, alliance = "a", visionRange = 500, atkType = "ranged", startNode = 4))

        # Team B
        self.creep.append(Creep(xPos = 3898, yPos = 350, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 21))
        self.creep.append(Creep(xPos = 4198, yPos = 450, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 21))
        self.creep.append(Creep(xPos = 3898, yPos = 450, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 21))
        self.creep.append(Creep(xPos = 3598, yPos = 450, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 21))
        self.creep.append(Creep(xPos = 3898, yPos = 550, wd = 40, ht = 40, atkRange = 250, alliance = "b", visionRange = 500, atkType = "ranged", startNode = 21))
        
        # Middle Lane
        # Team A
        self.creep.append(Creep(xPos = 900, yPos = 3996, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 26))
        self.creep.append(Creep(xPos = 900, yPos = 4096, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 26))
        self.creep.append(Creep(xPos = 930, yPos = 4096, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 26))
        self.creep.append(Creep(xPos = 870, yPos = 4096, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 26))
        self.creep.append(Creep(xPos = 900, yPos = 4196, wd = 40, ht = 40, atkRange = 250, alliance = "a", visionRange = 500, atkType = "ranged", startNode = 26))
        
        # Team B
        self.creep.append(Creep(xPos = 4005, yPos = 803, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 41))
        self.creep.append(Creep(xPos = 3705, yPos = 863, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 41))
        self.creep.append(Creep(xPos = 4005, yPos = 863, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 41))
        self.creep.append(Creep(xPos = 4305, yPos = 863, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 41))
        self.creep.append(Creep(xPos = 4005, yPos = 963, wd = 40, ht = 40, atkRange = 250, alliance = "b", visionRange = 500, atkType = "ranged", startNode = 41))
    
        # Bottom Lane
        # Team A
        self.creep.append(Creep(xPos = 1403, yPos = 4524, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 50))
        self.creep.append(Creep(xPos = 1103, yPos = 4624, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 50))
        self.creep.append(Creep(xPos = 1403, yPos = 4624, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 50))
        self.creep.append(Creep(xPos = 1703, yPos = 4624, wd = 40, ht = 40, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 50))
        self.creep.append(Creep(xPos = 1403, yPos = 4724, wd = 40, ht = 40, atkRange = 250, alliance = "a", visionRange = 500, atkType = "ranged", startNode = 50))
        
        # Team B
        self.creep.append(Creep(xPos = 4506, yPos = 919, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 66))
        self.creep.append(Creep(xPos = 4506, yPos = 1019, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 66))
        self.creep.append(Creep(xPos = 4206, yPos = 1019, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 66))
        self.creep.append(Creep(xPos = 4806, yPos = 1019, wd = 40, ht = 40, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 66))
        self.creep.append(Creep(xPos = 4506, yPos = 1119, wd = 40, ht = 40, atkRange = 250, alliance = "b", visionRange = 500, atkType = "ranged", startNode = 66))
