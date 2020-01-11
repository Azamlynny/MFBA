from PlayerTracker import *
from StructureTracker import *
from CreepTracker import *

class GameTracker():
    
    def __init__(self):
        self.PT = PlayerTracker() 
        self.ST = StructureTracker()
        self.CT = CreepTracker()
        self.res = 100 # resolution
        self.divis = 5000 / self.res
        self.grid = [[False for i in range(self.res)] for j in range(self.res)] 
        self.time = 0
        self.editingTree = False
        self.editingNodes = False
        
    def updateGrid(self, Game, Map):
        for o in range(self.res): # Reset grid
            for j in range(self.res):
                self.grid[j][o] = False
        
        for i in Game.PT.players:
            x = int(i.x / self.divis)
            y = int(i.y / self.divis)
            wd = int(i.wd / self.divis)
            ht = int(i.ht / self.divis)
            x -= wd / 2
            y -= ht / 2
            for o in range(y, y+ht):
                for j in range(x, x+wd):
                    self.grid[j][o] = True
        for i in Map.objects:
            x = int(i.x / self.divis)
            y = int(i.y / self.divis)
            wd = int(i.wd / self.divis)
            ht = int(i.ht / self.divis)
            # x -= wd / 2
            # y -= ht / 2    
            for o in range(y, y+ht):
                for j in range(x, x+wd):
                    self.grid[j][o] = True
        for i in Game.CT.creep:
            x = int(i.x / self.divis)
            y = int(i.y / self.divis)
            wd = int(i.wd / self.divis)
            ht = int(i.ht / self.divis)
            x -= wd / 2
            y -= ht / 2    
            for o in range(y, y+ht):
                for j in range(x, x+wd):
                    self.grid[j][o] = True
        
    def incTime(self):
        if(self.time % 1800 == 0):
            self.CT.spawnCreep()
        self.time += 1
        
                    
    def runDebuffs(self, Cam):
        if(self.time % 60 == 0):
            for i in self.PT.players:
                i.runDebuffs(self, Cam)
                
    def runProjectiles(self,Cam, Game):
        for i in self.PT.players:
            i.moveProjectiles(Cam, Game)
        for i in self.ST.structures:
            i.moveProjectiles(Cam, Game)
