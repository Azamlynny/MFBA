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
        self.ab1targetable = False
        self.ab2targetable = False

    def drawPlayer(self):
        if(self.name == "Dr. Fang"):
            fill(255, 255, 0)    
        elif(self.name == "Mr. Raite"):
            fill(82, 255, 249)
        elif(self.name == "Mrs. Gerstein"):
            fill(204, 0, 204)
        elif(self.name == "Dr. Jidarian"):
            fill(153, 255, 102)
        elif(self.name == "Mr. Weisser"):
            fill(0,0,102)
        elif(self.name == "Mr. Nowakowski"):
            fill(255, 218, 184)
        elif(self.name == "Mr. McMenamin"):
            fill(255, 153, 153)
        elif(self.name == "Mr. Sanservino"):
            fill(243, 110, 255)
        elif(self.name == "Mrs. Valley"):
            fill(255, 174, 0)
        elif(self.name == "Mr. Delprete"):
            fill(161, 136, 122)
            
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
    
    def drawRings(self):
        """Draw the range of your ability (if selected)"""
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
                self.target = None
                self.checkLevelUp()
            if(target.hp <= 0 and target.type == "tower"):
                self.xp += 220
                self.target = None
                self.checkLevelUp()
    
    def ability1(self, Game, Cam):
        """Activate ability 1 if selected and if in range"""
        return
        #remove and check mana (TODO)
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
        """Activate ability 1 if selected and if in range"""
        return
        #remove and check mana (TODO)
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
        """Check is xp is sufficient for level up, then process stats for leveling"""
        if (self.lvl < 25):
            if self.xp >= xpToLevel[self.lvl]:
                self.xp -= xpToLevel[self.lvl]
                self.lvl += 1
                #for now, all attributes increase by 5%
                self.atk += round(0.05 * self.atk)
                self.armor += round(0.05 * self.armor)
                self.strength += round(0.05 * self.strength)
                self.hp += int((0.05 * self.hpMax))
                self.hpMax += int((0.05 * self.hpMax))
                
    
    def checkHealth(self, Game, Cam):
        if self.hp <= 0 and not any(i.debuff == "dead" for i in self.debuffs):
            self.debuffs.append(Debuff("dead", self.hpRegen, respawnCooldown[self.lvl - 1]))
            self.hpRegen = 0
        elif any(i.debuff == "dead" for i in self.debuffs):
            self.x = self.respawnX
            self.y = self.respawnY
            for i in Game.PT.players:
                #print(i)
                if i.target == self:
                    i.target = None
            for i in Game.ST.structures:
                if i.target == self:
                    i.target = None
                    
