class Debuff:

    def __init__(self, debuff, modifier, time): # time is measured in seconds
        self.time = time
        self.debuff = debuff
        self.modifier = modifier
    
    def dec(self):
        """Decrease debuffs per game tick"""
        self.time -= 1 
        
