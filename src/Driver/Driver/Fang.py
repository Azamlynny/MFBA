from Player import *

class Fang(Player, object):
    def __init__(self, **kwds):
        super(Fang, self).__init__(**kwds)
        self.ab1range = 400
        self.ab2range = 250
        self.ab1cooldown = 1
        self.ab2cooldown = 120
        self.name = "Dr. Fang"
        self.ab1name = "Wormhole"
        self.ab2name = "EMP"
        
    def drawPlayer(self):
        fill(255,255,0)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        self.drawRings()
    
    def ability1(self, Game, Cam):
        tpx = mouseX - Cam.xshift
        tpy = mouseY - Cam.yshift
        if(self.distancePT(tpx,tpy) < self.ab1range ** 2 and (tpx <= 5000 and tpx >= 0) and (tpy <= 5000 and tpy >= 0)):
            print(tpx)
            print(tpy)
            self.x = tpx
            self.y = tpy
            self.xvel = 0
            self.yvel = 0
            self.ab1select = False
            self.debuffs.append(Debuff("ab1cd", 1, self.ab1cooldown))
        return
    
    def ability2(self, Game, Cam):
        silenceProcent = 0.5
        for i in range(1, len(Game.PT.players)):
            if(self.distance(Game.PT.players[i]) <= self.ab2range ** 2 and Game.PT.players[i].alliance != self.alliance):
                # TODO Implement check so that cooldown doesn't decrease
                Game.PT.players[i].debuffs.append(Debuff("ab1cd", 1, Game.PT.players[i].ab1cooldown * silenceProcent))
                Game.PT.players[i].debuffs.append(Debuff("ab2cd", 1, Game.PT.players[i].ab2cooldown * silenceProcent))
                self.ab2select = False
                self.debuffs.append(Debuff("ab2cd", 1, self.ab2cooldown))
        return
        
        
    def checkLevelUp(self):
        if (self.lvl < 25):
            if self.xp >= xpToLevel[self.lvl]:
                self.xp -= xpToLevel[self.lvl]
                self.lvl += 1
            
        
            
