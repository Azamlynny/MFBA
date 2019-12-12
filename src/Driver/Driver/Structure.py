from Attackable import *

class Structure(Entity):
    def __init__(self, strength, speed, hp, hpRegen, atk, armor, atkRange): #TODO: add debuffs
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.hpRegen = hpRegen
        self.atk = atk
        self.armor = armor
        self.atkRange = atkRange
        
    def basicAttack(self, target):
        """self does damage to a target"""
        distance = round(math.sqrt( (self.xPos - target.xPos)**2 + (self.yPos - target.yPos)**2))
        if distance > self.atkRange:
            pass
        else:
            mainDmg = (self.atk + self.strength)
            #TODO: add flat and percent bonuses after adding effects and debuffs
            armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
            target.hp -= round(mainDmg * armorMultiplier)
