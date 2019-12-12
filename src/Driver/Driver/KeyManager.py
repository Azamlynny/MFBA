class KeyManager():
    
    def __init__(self):
        self.inputs = [] 
        
    def keyInput(self, input):
        if(input not in self.inputs):
            self.inputs.append(input)    
    
    def keyRemove(self, input):
        self.inputs.remove(input)
        
    def runActions(self, Cam):
        if('w' in self.inputs):
            Cam.yshift += Cam.moveSpeed
        if('a' in self.inputs):
            Cam.xshift += Cam.moveSpeed            
        if('s' in self.inputs):
            Cam.yshift -= Cam.moveSpeed
        if('d' in self.inputs):
            Cam.xshift -= Cam.moveSpeed
