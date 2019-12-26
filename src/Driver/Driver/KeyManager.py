class KeyManager():
    
    def __init__(self):
        self.inputs = [] 
        
    def keyInput(self, input):
        if(input not in self.inputs):
            self.inputs.append(input)    
    
    def keyRemove(self, input):
        if(input in self.inputs):
            self.inputs.remove(input)    
        
    def runActions(self, Cam, Game):
        if('w' in self.inputs):
            Cam.yshift += Cam.moveSpeed
        if('a' in self.inputs):
            Cam.xshift += Cam.moveSpeed            
        if('s' in self.inputs):
            Cam.yshift -= Cam.moveSpeed
        if('d' in self.inputs):
            Cam.xshift -= Cam.moveSpeed
        if(' ' in self.inputs): # Space
            # TODO: bug needs fixing where nostroke() stops working once space is pressed
            Cam.xshift = -1 * Game.PT.players[0].x + 1960/2
            Cam.yshift = -1 * Game.PT.players[0].y + 1080/2
