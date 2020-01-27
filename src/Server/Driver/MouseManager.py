from Tree import *

class MouseManager():
    
    def __init__(self):
        self.player = 1
        self.treePlaceIndex = 0
        self.nodePlaceIndex = 0
                
    def middleClick(self, Cam):
        """Middle click pans camera"""
        Cam.xshift += mouseX - pmouseX
        Cam.yshift += mouseY - pmouseY
    
    def leftClick(self, Game, Cam, GUI, Map):
        """Run all functions for left click"""
        if(Game.editingTree):
            # Map Tree editor
            Map.objects.append(Tree(xPos = mouseX - Cam.xshift, yPos = mouseY - Cam.yshift, treeType = self.treePlaceIndex))
            self.treePlaceIndex+=1
            if(self.treePlaceIndex >= 5):
                self.treePlaceIndex-=5
        elif(Game.editingNodes):
            # Lane Node editor
            x = int(mouseX - Cam.xshift)
            y = int(mouseY - Cam.yshift)
            Map.laneNodes[self.nodePlaceIndex][0] = x
            Map.laneNodes[self.nodePlaceIndex][1] = y
            self.nodePlaceIndex+=1
            if(self.nodePlaceIndex >= 90):
                self.nodePlaceIndex = 0
        else:
            if(Game.PT.players[0].ab1select):
                if Game.PT.players[0].ab1targetable:
                    self.lockPlayerTarget(Game, Cam)
                Game.PT.players[0].ability1(Game, Cam)
            elif(Game.PT.players[0].ab2select):
                if Game.PT.players[0].ab2targetable:
                    self.lockPlayerTarget(Game, Cam)
                Game.PT.players[0].ability2(Game, Cam)
            else:
                for i in Game.PT.players:
                    if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2):
                        GUI.playerSlot = Game.PT.players.index(i)
                        GUI.type = "player"
                        return
                for i in Game.ST.structures:
                    if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2):
                        GUI.playerSlot = Game.ST.structures.index(i)
                        GUI.type = "structure"
                        return
                for i in Game.CT.creep:
                    if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2):
                        GUI.playerSlot = Game.CT.creep.index(i)
                        GUI.type = "creep"
                        return
                   
    # The server does not control a player but the client sends right click data to the server to manage
    def rightClick(self, Game, p, x, y): 

        # p = player 
        Game.PT.players[p].ab1select = False
        Game.PT.players[p].ab2select = False
        Game.PT.players[p].pathfindTo(x, y, Game)
        Game.PT.players[p].target = None
        for i in Game.PT.players:
            if(Game.PT.players[p].alliance != i.alliance):
                if(i == Game.PT.players[p]):
                    continue
                if(x >= i.x - i.wd/2 and x <= i.x + i.wd/2 and y >= i.y - i.ht/2 and y <= i.y + i.ht/2 and i.hp > 0):
                    Game.PT.players[p].target = i
                    return
        for i in Game.ST.structures:
            if(Game.PT.players[p].alliance != i.alliance):
                if(x >= i.x - i.wd/2 and x <= i.x + i.wd/2 and y >= i.y - i.ht/2 and y <= i.y + i.ht/2 and i.hp > 0):
                    Game.PT.players[p].target = i
                    return
        for i in Game.CT.creep:
            if(Game.PT.players[p].alliance != i.alliance):
                if(x >= i.x - i.wd/2 and x <= i.x + i.wd/2 and y >= i.y - i.ht/2 and y <= i.y + i.ht/2 and i.hp > 0):
                    Game.PT.players[p].target = i
                    return    
                
    #     Client exclusive function - Server does not control a player
    # def lockPlayerTarget(self, Game, Cam):
    #     """lock target for abilities"""
    #     player = Game.PT.players[0]
    #     for i in Game.PT.players:
    #         if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2): #if you clicked on a player
    #             if i.alliance != player.alliance:
    #                 player.target = i
    #             return
    #     for i in Game.ST.structures:
    #         if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2):
    #             if i.alliance != player.alliance:
    #                 player.target = i
    #             return
    #     # for i in Game.CT.creeps:
    #     #     if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2 and i.hp > 0):
    #     #         if i.alliance != player.alliance:
    #     #             player.target = i
    #     #         return
