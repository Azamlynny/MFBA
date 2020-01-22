from Player import *
class Sanservino(Player, object):
    def __init__(self, **kwds):
        super(Sanservino, self).__init__(**kwds)
        self.ab1range = 200
        self.ab2range = 200
        self.ab1cooldown = 1
        self.ab2cooldown = 60
        self.name = "Mr. Sanservino"
        self.ab1name = "Uhm..."
        self.ab2name = "Pop Quiz"
        self.ab1targetable = True
        self.ab2targetable = False
        
    def drawPlayer(self):
        fill(234, 41, 255)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        self.drawRings()
    
    def ability1(self, Game, Cam):
        if self.target != None:
            if self.distance(self.target) <= self.ab1range ** 2:
                self.target.debuffs.append(Debuff("stun", 1, 3))
                self.ab1select = False
                self.debuffs.append(Debuff("ab1cd", 1, self.ab1cooldown))
        return
    
    def ability2(self, Game, Cam):
        if self.target != None and self.target.type == "player":
            if self.distance(self.target) <= self.ab2range ** 2:
                self.target.hp -= self.atk + 100 #temp; think of a formula that's balanced
                if self.target.hp >= 0:
                    self.debuffs.append(Debuff("ab2cd", 1, self.ab2cooldown))
                self.ab2select = False
        return
    def checkLevelUp(self):
        if (self.lvl < 25):
            if self.xp >= xpToLevel[self.lvl]:
                self.xp -= xpToLevel[self.lvl]
                self.lvl += 1
