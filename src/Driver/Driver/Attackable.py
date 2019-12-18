from Entity import *
import math

class Attackable(Entity, object):
    
    def __init__(self, xPos, yPos, strength, speed, hp, hpRegen, atk, armor, atkRange, alliance, visionRange): #TODO: add debuffs
        super(Attackable, self).__init__(xPos, yPos)
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.hpRegen = hpRegen
        self.atk = atk
        self.armor = armor
        self.atkRange = atkRange
        self.alliance = alliance
        self.visionRange = visionRange

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
