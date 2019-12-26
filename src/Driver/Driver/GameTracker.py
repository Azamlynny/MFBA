from PlayerTracker import *

class GameTracker():
    
    def __init__(self):
        self.PT = PlayerTracker() 
        self.res = 200 # resolution 
        self.grid = [[False for i in range(self.res)] for j in range(self.res)] 
        
    def updateGrid(self, PT, Map):
        for o in range(self.res): # Reset grid
            for j in range(self.res):
                self.grid[j][o] = False
        
        for i in PT.players:
            x = int(i.x / 25)
            y = int(i.y / 25)
            wd = int(i.wd / 25)
            ht = int(i.ht / 25)
            x -= wd / 2
            y -= ht / 2
            for o in range(y, y+ht):
                for j in range(x, x+wd):
                    self.grid[j][o] = True
                    # fill(0)                    # Draw hitboxes
                    # rect(j * 10,o * 10,10,10)
                    
