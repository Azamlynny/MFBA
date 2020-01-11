from Mob import *

xpToLevel = {
    1:230,
    2:370,
    3:480,
    4:580,
    5:600,
    6:720,
    7:750,
    8:780,
    9:810,
    10:840,
    11:870,
    12:900,
    13:1225,
    14:1250,
    15:1275,
    16:1300,
    17:1325,
    18:1500,
    19:1590,
    20:1600,
    21:1850,
    22:2100,
    23:2350,
    24:2600,
    25:3500
}
respawnCooldown = [6, 8, 10, 14, 16, 26, 28, 30, 32, 34, 36, 44, 46, 48, 50, 52, 54, 65, 70, 75, 80, 85, 90, 95, 100]

class Player(Mob, object):
    def __init__(self, **kwds):
        super(Player, self).__init__(type = "player", **kwds)
        self.xp = 0
        self.lvl = 1
        self.gold = 0
        self.ab1select = False
        self.ab2select = False
        self.name = "Player"
        self.ab1name = "Ability 1"
        self.ab2name = "Ability 2"
        self.ab1cooldown = 10
        self.ab2cooldown = 10
        self.respawnX = self.x
        self.respawnY = self.y
        self.type = "player"

    def drawPlayer(self):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
    
    def drawRings(self):
        stroke(170, 178, 191)
        noFill()
        if(self.ab1select):
            ellipse(self.x, self.y, self.ab1range * 2, self.ab1range * 2)
        if(self.ab2select):
            ellipse(self.x, self.y, self.ab2range * 2, self.ab2range * 2)
    
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
            if(target.hp <= 0 and target.type == "player"):
                self.xp += target.lvl * 50 + 60
                self.checkLevelUp()
            if(target.hp <= 0 and target.type == "creep"):
                self.xp += 60
                self.checkLevelUp()
    
    def ability1(self, Game, Cam):
        return
        #remove and check mana
        # if self.checkRange(target):
        #     pass
        # elif self.alliance == target.alliance:
        #     pass
        # else:
        #     mainDmg = (self.atk + self.strength) * 1.5
        #     #TODO: add flat and percent bonuses after adding effects and debuffs
        #     armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
        #     target.hp -= round(mainDmg * armorMultiplier)
    
    def ability2(self, Game, Cam):
        return
        #remove and check mana
        # if self.checkRange(target):
        #     pass
        # elif self.alliance == target.alliance:
        #     pass
        # else:
        #     mainDmg = (self.atk + self.strength)
        #     #TODO: add flat and percent bonuses after adding effects and debuffs
        #     armorMultiplier = 1 - ((0.052 * target.armor)/(0.9 + 0.048 * abs(target.armor)))
        #     target.hp -= round(mainDmg * armorMultiplier)

    def checkLevelUp(self):
        if self.xp >= xpToLevel[self.lvl]:
            self.xp -= xpToLevel[self.lvl]
            self.lvl += 1
    
    def checkHealth(self, Game, Cam):
        if self.hp <= 0 and not any(i.debuff == "dead" for i in self.debuffs):
            self.debuffs.append(Debuff("dead", self.hpRegen, respawnCooldown[self.lvl - 1]))
            self.hpRegen = 0
        elif any(i.debuff == "dead" for i in self.debuffs):
            self.x = self.respawnX
            self.y = self.respawnY
            for i in Game.PT.players:
                print(i)
                if i.target == self:
                    i.target = None
            for i in Game.ST.structures:
                if i.target == self:
                    i.target = None
                    