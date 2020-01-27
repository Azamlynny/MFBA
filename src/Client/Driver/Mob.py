import math

from Attackable import *

class Mob(Attackable, object):
    def __init__(self, **kwds):
        super(Mob, self).__init__(**kwds)
        self.xvel = 0
        self.yvel = 0
        self.goalx = None
        self.goaly = None
      
    def pathfindTo(self,x,y,Game):
        """Pathfind to a certain x and y position"""
        self.goalx = x
        self.goaly = y
        dist = math.sqrt((y-self.y)**2 + (x-self.x)**2)
        time = dist / self.speed
        if(time != 0):
            self.xvel = (x - self.x) / time
            self.yvel = (y - self.y) / time
        else:
            self.xvel = 0
            self.yvel = 0
    
    def move(self, Game):
        """Move objects and check hitboxes"""
        if(self.xvel != 0 or self.yvel != 0) and not any(i.debuff == "stun" for i in self.debuffs): # Only performs hitbox checks for moving objects
            if(abs(self.x - self.goalx) < 5 and abs(self.y - self.goaly) < 5): # Stop the object when it reaches its goal with a small tolerance
                self.xvel = 0
                self.yvel = 0
            else: 
                # Check hitbox collisions before moving the object
                tempx = self.x + self.xvel
                tempy = self.y + self.yvel
                sclx = int(tempx / Game.divis)
                scly = int(tempy / Game.divis)
                if(self.xvel > 0 and Game.grid[sclx + int(self.wd / (Game.divis * 2)) + 1][scly] == True):
                    self.xvel = 0
                    self.yvel = 0
                if(self.xvel < 0 and Game.grid[sclx - int(self.wd / (Game.divis * 2)) - 1][scly] == True):
                    self.xvel = 0
                    self.yvel = 0
                if(self.yvel > 0 and Game.grid[sclx][scly + int(self.ht / (Game.divis * 2)) + 1] == True):
                    self.yvel = 0
                    self.xvel = 0
                if(self.yvel < 0 and Game.grid[sclx][scly - int(self.ht / (Game.divis * 2)) - 1] == True):
                    self.yvel = 0
                    self.xvel = 0
                if(self.atkCooldown < 10):
                    # Backswing to prevent attacking then instantly moving
                    self.x += self.xvel
                    self.y += self.yvel
