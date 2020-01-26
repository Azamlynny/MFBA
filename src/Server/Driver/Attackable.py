from Entity import *
from Projectile import *
from Debuff import *
from Util import *
import math

class Attackable(Entity, object):
    
    def __init__(self, strength, speed, hp, hpMax, hpRegen, atk, atkSpeed, armor, atkRange, alliance, visionRange, atkType, type = "", projWidth = 10, **kwds): #TODO: add debuffs
        super(Attackable, self).__init__(**kwds)
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
        self.atkType = atkType
        self.projWidth = projWidth
        self.target = None
        self.atkCooldown = 0
        self.debuffs = []
        self.projectiles = []
        self.type = type

        # For GUI to function
        self.ab1select = False
        self.ab2select = False
        self.name = "Attackable"
        self.ab1name = " "
        self.ab2name = " "
        self.ab1cooldown = 10
        self.ab2cooldown = 10
    
    def distance(self, target):
        """Distance formula between self and target, squared so we can keep working with ints"""
        return (self.x - target.x)**2 + (self.y - target.y)**2

    def checkRange(self, target):
        """Checks if target is within self's range"""
        if self.distance(target) > self.atkRange**2:
            return True
        return False
    
    def defaultAttack(self, Game):
        """Check if conditions are correct for attack, then executes basicAttack or projectileAttack if they are"""
        if(self.atkCooldown <= 0 and self.target != None):
            if self.checkRange(self.target):
                pass
            elif self.alliance == self.target.alliance:
                pass
            else:
                if(self.atkType == "ranged"):
                    self.projectileAttack(Game, self.target)
                else:
                    self.basicAttack(self.target)
                self.atkCooldown += 60 / self.atkSpeed    
        elif(self.atkCooldown > 0):
            self.atkCooldown -= 1  
            
            
    def basicAttack(self, target):
        """self does damage to a target"""
        self.xvel = 0
        self.yvel = 0                
        mainDmg = (self.atk + self.strength)
        #TODO: add flat and percent bonuses after adding effects and debuffs
        armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor))) #this formula is a simplified version from Dota's
        target.hp -= round(mainDmg * armorMultiplier)
        if(target.hp <= 0):
            self.target = None

    def projectileAttack(self, Game, Target):
        """Spawn Projectile that follows player"""
        self.xvel = 0
        self.yvel = 0
        self.projectiles.append(Projectile(self.x,self.y, self.projWidth, 10, Game, Target))
        if(Target.hp <= 0):
            self.target = None

    def drawHealth(self):
        """Draw health bar above player"""
        fill(0,0,0)
        rect(self.x - self.wd/2, self.y - (self.ht - 5), self.wd, 5, 5, 5, 5, 5)
        
        if(self.alliance == "a"):
            fill(0,204,20)
        else:
            fill(255,0,0)
        if self.hp >= 0:
            rect(self.x - self.wd/2, self.y - (self.ht-5), round(self.wd * self.hp/self.hpMax), 5, 5, 5, 5, 5)
            
    def runDebuffs(self, Game, Cam):
        """Check various debuff effects and process their cooldowns"""
        
        #Healing
        if(self.hp + self.hpRegen <= self.hpMax):
            self.hp += self.hpRegen
        else:
            self.hp = self.hpMax
        
        # Debuff effects locally change stats in players skills
        
        for i in self.debuffs:
            i.dec()
            if(i.time <= 0):
                # Reset Stats after death debuff expires
                if self.type == "player" and i.debuff == "dead":
                    self.target = None
                    self.hp = self.hpMax
                    if Game.PT.players[0] == self:
                        #reset Camera focus
                        Cam.xshift = -1 * Game.PT.players[0].x + 1960/2
                        Cam.yshift = -1 * Game.PT.players[0].y + 1080/2
                    self.hpRegen = i.modifier #hpRegen is set to 0 when dead so the gui looks correct
            self.debuffs.remove(i) #once debuff expires, remove debuff from the Attackable
            
    def moveProjectiles(self, Cam, Game):
        """Move projectiles, check for collision, and dodo basicAttack once hit"""
        for i in self.projectiles:
            if any(j.debuff == "dead" for j in i.Target.debuffs):
                self.projectiles.remove(i)
            i.move(Game)
            if(sd(Cam,i.x,i.y,i.wd,i.wd)):
                i.drawProjectile()
            if(round(math.sqrt((i.x - i.Target.x)**2 + (i.y - i.Target.y)**2)) < 15): # 15 pixel tolerance for projectiles colliding
                self.basicAttack(i.Target)
                if(i in self.projectiles):
                    self.projectiles.remove(i)
