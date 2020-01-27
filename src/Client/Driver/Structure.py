from Attackable import *

class Structure(Attackable, object):
    def __init__(self, **kwds):
        super(Structure, self).__init__(**kwds)
        self.name = "Structure"    
                
class Nexus(Structure, object):
    def __init__(self, **kwds):
        super(Nexus, self).__init__(wd = 150, ht = 150, strength = 5, speed = 0, hp = 1000, hpMax = 1000, hpRegen = 5, atk = 0, atkSpeed = 0.0, armor = 5, atkRange = 0, visionRange = 650, atkType = "none", projWidth = 0, type = "nexus", **kwds)
        self.name = "Nexus"
        
    def checkDead(self, Game, Cam):
        if Game.winner != None:
            #for whenever a very close race where both teams are on the nexus happens
            return
        if self.hp <= 0:
            if self.alliance == "a":
                Game.winner = "b"
            elif self.alliance == "b":
                Game.winner = "a"
    
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
        if(self.hp > 0):
            self.drawHealth()

class Tower(Structure, object):
    def __init__(self, **kwds):
        super(Tower, self).__init__(wd = 100, ht = 100, strength = 5, speed = 5, hp = 1000, hpMax = 1000, hpRegen = 0, atk = 50, atkSpeed = 1.0, armor = 5, atkRange = 500, visionRange = 650, atkType = "ranged", projWidth = 25, type = "tower", **kwds)
        self.name = "Tower"
        self.type = "tower"

    def lockTarget(self, Game):
        if(self.hp > 0):
            for i in Game.CT.creep:
                if self.distance(i) <= self.atkRange ** 2 and self.alliance != i.alliance:
                    self.target = i
                    return
                else:
                    self.target = None
            for i in Game.PT.players:
                if self.distance(i) <= self.atkRange ** 2 and self.alliance != i.alliance:
                    self.target = i
                    return
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
