from Entity import *
import math

class Attackable(Entity, object):
    
    def __init__(self, xPos, yPos, wd, ht, strength, speed, hp, hpMax, hpRegen, atk, atkSpeed, armor, atkRange, alliance, visionRange): #TODO: add debuffs
        super(Attackable, self).__init__(xPos, yPos, wd, ht)
        self.hpMax = hpMax
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.hpRegen = hpRegen
        self.atk = atk
        self.atkSpeed = atkSpeed
        self.armor = armor
        self.atkRange = atkRange
        self.alliance = alliance
        self.visionRange = visionRange
        self.target = None
        self.atkCooldown = 0
        self.debuffs = []
    
    def distance(self, target):
        return round(math.sqrt((self.x - target.x)**2 + (self.y - target.y)**2))

    def checkRange(self, target):
        if self.distance(target) > self.atkRange:
            return True
        return False
    
    def defaultAttack(self, Game):
        if(self.target != None):
            if(self.atkCooldown <= 0):
                for i in range (0, len(Game.PT.players)):
                    if(self.target == Game.PT.players[i]):
                        targetIndex = i
                self.basicAttack(Game.PT.players[i])
                self.atkCooldown += self.atkSpeed * 60     
            else:
                self.atkCooldown -= 1  
            
            
    def basicAttack(self, target):
        """self does damage to a target"""
        if self.checkRange(target):
            pass
        elif self.alliance == target.alliance:
            pass
        else:
            self.xvel = 0
            self.yvel = 0
            mainDmg = (self.atk + self.strength)
            #TODO: add flat and percent bonuses after adding effects and debuffs
            armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
            target.hp -= round(mainDmg * armorMultiplier)

    def drawHealth(self):
        fill(0,0,0)
        rect(self.x - self.wd/2, self.y - (self.ht - 5), self.wd, 5, 5, 5, 5, 5)
        
        if(self.alliance == "a"):
            fill(0,204,20)
        else:
            fill(255,0,0)
        if self.hp >= 0:
            rect(self.x - self.wd/2, self.y - (self.ht-5), round(self.wd * self.hp/self.hpMax), 5, 5, 5, 5, 5)
            
    def runDebuffs(self):
        if(self.hp + self.hpRegen <= self.hpMax):
            self.hp += self.hpRegen
        else:
            self.hp = self.hpMax
        
        for i in self.debuffs:
            i.dec()
