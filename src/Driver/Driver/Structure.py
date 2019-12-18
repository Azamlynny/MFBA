from Attackable import *

class Structure(Attackable, object):
    def __init__(self, xPos, yPos, strength, speed, hp, hpRegen, atk, armor, atkRange, alliance):
        super(Structure, self).__init__(xPos, yPos, strength, speed, hp, hpRegen, atk, armor, atkRange, alliance)
        self.speed = 0
    
class Nexus(Structure):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.atk = 0

class Tower(Structure):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.range = 1000
    
    #TODO: player targeting - needs movemment system first
