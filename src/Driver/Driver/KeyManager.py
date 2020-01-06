class KeyManager():
    
    def __init__(self):
        self.inputs = [] 
        self.outputted = False
        
    def keyInput(self, input):
        if(input not in self.inputs):
            self.inputs.append(input)    
    
    def keyRemove(self, input):
        if(input in self.inputs):
            self.inputs.remove(input)    
        
    def runActions(self, Cam, Game, Map):
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
        if('q' in self.inputs and not (any(i.debuff == "ab1cd" for i in Game.PT.players[0].debuffs))):
            Game.PT.players[0].ab1select = True
            Game.PT.players[0].ab2select = False
        if('e' in self.inputs and not (any(i.debuff == "ab2cd" for i in Game.PT.players[0].debuffs))):
            Game.PT.players[0].ab2select = True
            Game.PT.players[0].ab1select = False
        if('o' in self.inputs and Game.editing):
            if(self.outputted == False):
                self.fo = open("map.txt", "w")
                self.outputted = True
                for i in Map.objects:
                    output = str(i.x) + " " + str(i.y) + " " + str(i.treeType) + "\n"
                    self.fo.write(output)
                self.fo.close()
        if('t' in self.inputs and Game.editing):
            if(len(Map.objects) > 0):
                Map.objects.pop()    
        if('j' in self.inputs and 'k' in self.inputs and 'l' in self.inputs):
            if(Game.editing == False):
                Game.editing = True
            else:
                Game.editing = False
        # if('65535' in self.inputs): # Alt
