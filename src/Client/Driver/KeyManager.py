class KeyManager():
    
    def __init__(self):
        self.inputs = [] 
        self.outputted = False
        
    def keyInput(self, input):
        """Adds key to inputs list"""
        if(input not in self.inputs):
            self.inputs.append(input)    
    
    def keyRemove(self, input):
        """Removes key from inputs list"""
        if(input in self.inputs):
            self.inputs.remove(input)    
        
    def runActions(self, Cam, Game, Map, MManage):
        """Process all key pressed actions"""
        p = Game.player
        
        # Pan Camera with WASD
        if('w' in self.inputs):
            Cam.yshift += Cam.moveSpeed
        if('a' in self.inputs):
            Cam.xshift += Cam.moveSpeed            
        if('s' in self.inputs):
            Cam.yshift -= Cam.moveSpeed
        if('d' in self.inputs):
            Cam.xshift -= Cam.moveSpeed
        
        
        if(p != None):
            if(' ' in self.inputs): # Space
                Cam.xshift = -1 * Game.PT.players[p].x + 1960/2
                Cam.yshift = -1 * Game.PT.players[p].y + 1080/2
            
            # Abilities didn't work out in the end.
            # if('q' in self.inputs and not (any(i.debuff == "ab1cd" for i in Game.PT.players[0].debuffs))):
            #     Game.PT.players[p].ab1select = True
            #     Game.PT.players[p].ab2select = False
            # if('e' in self.inputs and not (any(i.debuff == "ab2cd" for i in Game.PT.players[0].debuffs))):
            #     Game.PT.players[p].ab2select = True
            #     Game.PT.players[p].ab1select = False
            
            if('`' in self.inputs):
                Game.PT.players[p].ab2select = False
                Game.PT.players[p].ab1select = False
            if('65535' in self.inputs): # Alt
                Cam.drawRings = True
            else:
                Cam.drawRings = False
            
                # Developer tools exclusive to the Server - Client cannot access    
            # if('o' in self.inputs and Game.editingTree):
            #     if(self.outputted == False):
            #         self.fo = open("map.txt", "w")
            #         self.outputted = True
            #         for i in Map.objects:
            #             output = str(i.x) + " " + str(i.y) + " " + str(i.treeType) + "\n"
            #             self.fo.write(output)
            #         self.fo.close()
            #         print("Saved Trees")
            # if('t' in self.inputs and Game.editingTree):
            #     if(len(Map.objects) > 0):
            #         Map.objects.pop()    
            # if('j' in self.inputs and 'k' in self.inputs and 'l' in self.inputs):
            #     if(Game.editingTree == False):
            #         Game.editingTree = True
            #     else:
            #         Game.editingTree = False
            # if('h' in self.inputs and 'j' in self.inputs and 'k' in self.inputs):
            #     if(Game.editingNodes == False):
            #         Game.editingNodes = True
            #         print("editing nodes")
            #     else:
            #         Game.editingNodes = False
            #         print("stopped editing nodes")
            # if('p' in self.inputs and Game.editingNodes):
            #     if(self.outputted == False):
            #         self.fo = open("lane_nodes.txt", "w")
            #         self.outputted = True
            #         for i in Map.laneNodes:
            #             output = str(i[0]) + " " + str(i[1]) + "\n"
            #             self.fo.write(output)
            #         self.fo.close()
            #         print("Saved Lane Nodes")
            # if('-' in self.inputs and Game.editingNodes):
            #     MManage.nodePlaceIndex-=1
            # if('=' in self.inputs and Game.editingNodes):
            #     MManage.nodePlaceIndex+=1
