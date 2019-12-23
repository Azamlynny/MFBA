from PlayerTracker import *

class GameTracker():
    
    def __init__(self):
        self.PT = PlayerTracker() 
        self.res = 5000 # resolution 
        self.grid = [[False for i in range(self.res)] for j in range(self.res)] 
        
   
