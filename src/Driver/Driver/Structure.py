from Attackable import *

class Structure(Attackable):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.speed = 0
    
class Nexus(Structure):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.atk = 0

class Tower(Structure):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.range = 1000