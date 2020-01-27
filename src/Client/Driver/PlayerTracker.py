from Player import * 
# Fang and Sanservino are not used now
# from Fang import *
# from Sanservino import *
from Util import *

class PlayerTracker():

    def __init__(self):
        self.players = []
        self.projx = [] # For projectiles
        self.projy = [] # For projectiles
        self.projwd = [] # For projectiles
        
        # Team A
        self.players.append(Player(xPos = 100, yPos = 4500, wd = 60, ht = 60, strength = 7, speed = 7, hp = 250, hpMax = 250, hpRegen = 2, atk = 15, atkSpeed = 3, armor = 3, atkRange = 400, alliance = "a", visionRange = 750, atkType = "ranged"))
        self.players.append(Player(xPos = 200, yPos = 4600, wd = 80, ht = 80, strength = 5, speed = 6, hp = 500, hpMax = 500, hpRegen = 4, atk = 35, atkSpeed = 1.0, armor = 5, atkRange = 100, alliance = "a", visionRange = 600, atkType = "melee"))     
        self.players.append(Player(xPos = 300, yPos = 4700, wd = 60, ht = 60, strength = 7, speed = 8, hp = 350, hpMax = 350, hpRegen = 2, atk = 40, atkSpeed = 2, armor = 3, atkRange = 125, alliance = "a", visionRange = 600, atkType = "melee"))
        self.players.append(Player(xPos = 400, yPos = 4800, wd = 70, ht = 70, strength = 5, speed = 6, hp = 350, hpMax = 350, hpRegen = 4, atk = 35, atkSpeed = 1.5, armor = 3, atkRange = 100, alliance = "a", visionRange = 500, atkType = "melee"))        
        self.players.append(Player(xPos = 500, yPos = 4900, wd = 70, ht = 70, strength = 5, speed = 7, hp = 450, hpMax = 450, hpRegen = 3, atk = 35, atkSpeed = 1.5, armor = 3, atkRange = 450, alliance = "a", visionRange = 500, atkType = "ranged"))
        # Team B
        self.players.append(Player(xPos = 4500, yPos = 100, wd = 80, ht = 80, strength = 5, speed = 5, hp = 500, hpMax = 500, hpRegen = 4, atk = 35, atkSpeed = 1.5, armor = 5, atkRange = 100, alliance = "b", visionRange = 600, atkType = "melee"))
        self.players.append(Player(xPos = 4600, yPos = 200, wd = 60, ht = 80, strength = 5, speed = 7, hp = 450, hpMax = 450, hpRegen = 3, atk = 35, atkSpeed = 1.5, armor = 3, atkRange = 450, alliance = "b", visionRange = 600, atkType = "ranged"))
        self.players.append(Player(xPos = 4700, yPos = 300, wd = 65, ht = 65, strength = 10, speed = 6, hp = 200, hpMax = 200, hpRegen = 3, atk = 85, atkSpeed = 0.75, armor = 3, atkRange = 125, alliance = "b", visionRange = 500, atkType = "melee"))
        self.players.append(Player(xPos = 4800, yPos = 400, wd = 45, ht = 45, strength = 7, speed = 7, hp = 350, hpMax = 350, hpRegen = 2, atk = 40, atkSpeed = 2, armor = 3, atkRange = 125, alliance = "b", visionRange = 750, atkType = "melee"))
        self.players.append(Player(xPos = 4900, yPos = 500, wd = 50, ht = 50, strength = 7, speed = 9, hp = 350, hpMax = 350, hpRegen = 3, atk = 40, atkSpeed = 1.5, armor = 3, atkRange = 300, alliance = "b", visionRange = 500, atkType = "ranged"))
        
        # Team A
        self.players[0].name = "Dr. Fang" # High vision range and dps, low hp
        self.players[1].name = "Mr. Raite" # Tanky
        self.players[2].name = "Mrs. Gerstein" # Really fast, high attack
        self.players[3].name = "Dr. Jidarian" # High damage
        self.players[4].name = "Mr. Weisser" # Well Rounded
        
        # Team B
        self.players[5].name = "Mr. Nowakowski" # Tanky
        self.players[6].name = "Mr. McMenamin" # Well rounded
        self.players[7].name = "Mr. Sanservino" # Glass cannon
        self.players[8].name = "Mrs. Valley" # Really high vision range
        self.players[9].name = "Mr. Delprete" # Very fast
     
    def drawPlayers(self, Cam, Alliance):
        """Draw players and their healths"""
        scale = 5000 / Alliance.resolution
        for i in self.players:
            if(sd(Cam,i.x,i.y,i.wd,i.ht)):
                if(Alliance.vision[int(i.x / scale)][int(i.y / scale)]):
                    if any(j.debuff == "dead" for j in i.debuffs) or i.hp <= 0:
                        pass 
                    else:    
                        i.drawPlayer()
                        i.drawHealth()
                
    def drawProjectiles(self, Cam, Alliance):
        """Draw projectiles"""
        scale = 5000 / Alliance.resolution
        for i in range(0,len(self.projx)):
            if(sd(Cam,self.projx[i],self.projy[i],self.projwd[i],self.projwd[i])):
                if(Alliance.vision[int(self.projx[i] / scale)][int(self.projy[i] / scale)]):
                    fill(0)
                    ellipse(self.projx[i],self.projy[i],self.projwd[i],self.projwd[i])
    
    def runPlayerActions(self, Game, Cam):
        """Run all player-related functions"""
        for i in self.players:
            i.defaultAttack(Game)
            i.checkHealth(Game, Cam)
    def updateMoving(self, Game):
        """Update and move players"""
        for i in self.players:
            i.move(Game)
