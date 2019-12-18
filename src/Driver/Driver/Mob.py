from Attackable import *

class Mob(Attackable, object):
    def __init__(self, **kwds):
        super(Mob, self).__init__(**kwds)
    
    def pathfindTo(self,x,y):
        self.x = x
        self.y = y
