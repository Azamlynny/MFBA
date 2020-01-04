import math

class Projectile:

    def __init__(self, x, y, wd, speed, Game, Target): # time is measured in seconds
        self.x = x
        self.y = y
        self.wd = wd
        self.speed = speed
        self.Target = Target
        for i in range(0,len(Game.PT.players)):
            if(self.Target == Game.PT.players[i]):
                self.index = i
        
    def move(self, Game):
        self.Target = Game.PT.players[self.index]
        xdist = self.Target.x - self.x
        ydist = self.Target.y - self.y
        distance = round(math.sqrt((self.x - self.Target.x)**2 + (self.y - self.Target.y)**2))
        time = distance / self.speed
        
        self.xvel =  xdist / time
        self.yvel =  ydist / time
        self.x += self.xvel
        self.y += self.yvel            
        
    def drawProjectile(self):
        fill(0)
        ellipse(self.x-5, self.y-5, self.wd, self.wd)
    
