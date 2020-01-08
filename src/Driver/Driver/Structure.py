from Attackable import *

class Structure(Attackable, object):
    def __init__(self, **kwds):
        super(Structure, self).__init__(**kwds)
        self.name = "Structure"    
                
class Nexus(Structure):
    def __init__(self, **kwds):
        super().__init__(type = "nexus", **kwds)
        self.atk = 0

class Tower(Structure, object):
    def __init__(self, **kwds):
        super(Tower, self).__init__(wd = 100, ht = 100, strength = 5, speed = 5, hp = 1000, hpMax = 1000, hpRegen = 0, atk = 50, atkSpeed = 1.0, armor = 5, atkRange = 500, visionRange = 650, atkType = "ranged", projWidth = 25, type = "tower", **kwds)
        self.name = "Tower"
        self.type = "tower"

    def lockTarget(self, Game):
        if(self.hp > 0):
            for i in Game.PT.players:
                if self.distance(i) <= self.atkRange ** 2 and self.alliance != i.alliance:
                    # print(self.distance(i))
                    # print(self.atkRange)
                    # print(i)
                    self.target = i
                    break
                else:
                    self.target = None
        else:
            self.target = None
            
                
    def defaultAttack(self, Game):
        if(self.atkCooldown <= 0 and self.target != None):
            if(self.atkType == "ranged"):
                self.projectileAttack(Game, self.target)
            else:
                self.basicAttack(Game.PT.players[i])
            self.atkCooldown += 60 / self.atkSpeed    
        elif(self.atkCooldown > 0):
            self.atkCooldown -= 1  
    
    def drawStructure(self, Cam):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)
        if(self.hp <= 0):
            fill(50)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        #draw range
        noFill()
        if(self.alliance == "a"):
            stroke(0,0,255)
        elif(self.alliance == "b"):
            stroke(255,0,0)
        else:
            stroke(0,255,0)
        if(Cam.drawRings and self.hp > 0):
            circle(self.x, self.y, self.atkRange * 2)
        noStroke()
        if(self.hp > 0):
            self.drawHealth()
