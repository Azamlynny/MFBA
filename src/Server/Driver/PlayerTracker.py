from Player import * 
from Fang import *
from Sanservino import *
from Util import *

class PlayerTracker():

    def __init__(self):
        self.players = []
        # Team A
        self.players.append(Fang(xPos = 100, yPos = 4500, wd = 50, ht = 50, strength = 5, speed = 12, hp = 250, hpMax = 250, hpRegen = 250, atk = 60, atkSpeed = 4.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 700, atkType = "ranged"))
        self.players.append(Player(xPos = 200, yPos = 4600, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee"))        
        self.players.append(Player(xPos = 300, yPos = 4700, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee"))
        self.players.append(Player(xPos = 400, yPos = 4800, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee"))        
        self.players.append(Player(xPos = 500, yPos = 4900, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee"))
        # Team B
        self.players.append(Player(xPos = 4500, yPos = 100, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee"))        
        self.players.append(Player(xPos = 4600, yPos = 200, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee"))
        self.players.append(Player(xPos = 4700, yPos = 300, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee"))        
        self.players.append(Player(xPos = 4800, yPos = 400, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee"))
        self.players.append(Player(xPos = 4900, yPos = 500, wd = 70, ht = 70, strength = 5, speed = 3, hp = 450, hpMax = 500, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500, atkType = "melee"))
     
    def drawPlayers(self, Cam, Alliance):
        """Draw players and their healths"""
        scale = 5000 / Alliance.resolution
        for i in self.players:
            if(sd(Cam,i.x,i.y,i.wd,i.ht)):
                if(Alliance.vision[int(i.x / scale)][int(i.y / scale)]):
                    if not any(j.debuff == "dead" for j in i.debuffs): #check if they're dead, and don't draw them if they are
                        i.drawPlayer()
                        i.drawHealth()
                
    def runPlayerActions(self, Game, Cam):
        for i in self.players:
            i.defaultAttack(Game)
            i.checkHealth(Game, Cam)
    def updateMoving(self, Game):
        for i in self.players:
            i.move(Game)
