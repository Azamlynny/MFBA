from Mob import *

class Creep(Mob, object):
    
    def __init__(self, **kwds):
        super(Player, self).__init__(type = "creep", **kwds)
    
