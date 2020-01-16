import math

class Projectile:

    def __init__(self, x, y, wd, speed, Game, Target): # time is measured in seconds
        self.x = x
        self.y = y
        self.wd = wd
        self.speed = speed
        self.Target = Target
        self.type = None
        for i in range(0,len(Game.PT.players)):
            if(self.Target == Game.PT.players[i]):
                self.index = i
                self.type = "player"
        for i in range(0,len(Game.ST.structures)):
            if(self.Target == Game.ST.structures[i]):
                self.index = i
                self.type = "structure"
        
    def move(self, Game):
        if(self.type == "player"):
            self.Target = Game.PT.players[self.index]
        elif(self.type == "structure"):
            self.Target = Game.ST.structures[self.index]
        xdist = self.Target.x - self.x
        ydist = self.Target.y - self.y
        distance = round(math.sqrt((self.x - self.Target.x)**2 + (self.y - self.Target.y)**2))
        time = distance / self.speed
        if(time > 0):
            self.xvel =  xdist / time
            self.yvel =  ydist / time
        else:
            self.xvel = 0
            self.yvel = 0
        self.x += self.xvel
        self.y += self.yvel            
        
    def drawProjectile(self):
        fill(0)
        ellipse(self.x-5, self.y-5, self.wd, self.wd)
    
