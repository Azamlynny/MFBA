from Entity import *
import math

class Attackable(Entity, object):
    
    def __init__(self, xPos, yPos, strength, speed, hp, hpMax, hpRegen, atk, armor, atkRange, alliance, visionRange): #TODO: add debuffs
        super(Attackable, self).__init__(xPos, yPos)
        self.hpMax = hpMax
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.hpRegen = hpRegen
        self.atk = atk
        self.armor = armor
        self.atkRange = atkRange
        self.alliance = alliance
        self.visionRange = visionRange
        self.target = None
    
    def distance(self, target):
        return round(math.sqrt( (self.xPos - target.xPos)**2 + (self.yPos - target.yPos)**2))

    def checkRange(self, target):
        if self.distance(target) > self.atkRange:
            return True
        return False

    def basicAttack(self, target):
        """self does damage to a target"""
        if self.checkRange(target):
            pass
        elif self.alliance == target.alliance:
            pass
        else:
            mainDmg = (self.atk + self.strength)
            #TODO: add flat and percent bonuses after adding effects and debuffs
            # armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
            target.hp -= round(mainDmg * armorMultiplier)
            
    def drawHealth(self):
        fill(0,0,0)
        rect(self.x - self.wd/2, self.y - 51, 50, 5, 5, 5, 5, 5)
        
        if(self.alliance == "a"):
            fill(0,204,20)
        else:
            fill(255,0,0)
        rect(self.x - self.wd/2, self.y - 51, round(50 * self.hp/self.hpMax), 5, 5, 5, 5, 5)
    def drawHealth(self):
        fill(0,0,0)
        rect(self.x - self.wd/2, self.y - 51, 50, 5, 5, 5, 5, 5)
        
        if(self.alliance == "a"):
            fill(0,204,20)
        else:
            fill(255,0,0)
        if self.hp >= 0:
            rect(self.x - self.wd/2, self.y - 51, round(50 * self.hp/self.hpMax), 5, 5, 5, 5, 5)
