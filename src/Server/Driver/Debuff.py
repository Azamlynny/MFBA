class Debuff:

    def __init__(self, debuff, modifier, time): # time is measured in seconds
        self.time = time #how long the debuff lasts
        self.debuff = debuff #name of debuff
        self.modifier = modifier #used as a way to store stats if they're altered
    
    def dec(self): 
        """Decrease debuffs per game tick"""
        self.time -= 1 
        
