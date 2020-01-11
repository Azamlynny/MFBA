from Creep import * 
from Util import *

class CreepTracker():

    def __init__(self):
        self.creep = []
                  
    def drawCreep(self, Cam, Alliance):
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
        for i in self.creep:
            if(i.hp <= 0):
                if(GUI.type == "creep"):
                    GUI.playerSlot = 0
                    GUI.type = "player"
                self.creep.remove(i)
            i.runAI(Game, Map)
    
    def spawnCreep(self):
        # Team A
        self.creep.append(Creep(xPos = 340, yPos = 3601, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 300, yPos = 3601, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 370, yPos = 3601, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 340, yPos = 3601, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee", startNode = 4))
        self.creep.append(Creep(xPos = 340, yPos = 3601, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 250, alliance = "a", visionRange = 500, atkType = "ranged", startNode = 4))

        # Team B
        self.creep.append(Creep(xPos = 3345, yPos = 519, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 20))
        self.creep.append(Creep(xPos = 3345, yPos = 519, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 20))
        self.creep.append(Creep(xPos = 3345, yPos = 519, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 20))
        self.creep.append(Creep(xPos = 3345, yPos = 519, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee", startNode = 20))
        self.creep.append(Creep(xPos = 3345, yPos = 519, wd = 40, ht = 40, strength = 5, speed = 5, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 9, atkSpeed = 1.0, armor = 3, atkRange = 250, alliance = "b", visionRange = 500, atkType = "ranged", startNode = 20))
