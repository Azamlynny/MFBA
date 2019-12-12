from Entity import *
import math

class Attackable(Entity):
    
    def __init__(self, strength, speed, hp, hpRegen, atk, armor, atkRange, alliance, **kwds): #TODO: add debuffs
        super().__init__(**kwds)
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.hpRegen = hpRegen
        self.atk = atk
        self.armor = armor
        self.atkRange = atkRange
        self.alliance = alliance
    
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
            armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
            target.hp -= round(mainDmg * armorMultiplier)