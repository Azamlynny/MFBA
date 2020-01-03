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

class Player(Mob, object):
    def __init__(self, **kwds):
        super(Player, self).__init__(**kwds)
        self.xp = 0
        self.lvl = 1
        self.gold = 0
        self.ab1select = False
        self.ab2select = False
        self.name = "Player"

    def drawPlayer(self):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
    
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
            if(target.hp <= 0):
                self.xp += target.lvl * 50 + 60
                self.checkLevelUp()
    
    def ability1(self, Cam):
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
    
    def ability2(self, Cam):
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
            
        
            
