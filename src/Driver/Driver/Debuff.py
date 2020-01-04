class Debuff:

    def __init__(self, debuff, modifier, time): # time is measured in seconds
        self.time = time
        self.debuff = debuff
        self.modifier = modifier
    
    def dec(self): 
        self.time -= 1
        
