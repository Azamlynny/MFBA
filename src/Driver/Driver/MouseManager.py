from Tree import *
from Node import *

class MouseManager():
    
    def __init__(self):
        self.player = 1
        self.treePlaceIndex = 0
        self.nodePlaceIndex = 0
        self.currNode = 0
        self.coneNode = 0
        self.makingConnections = False
                
    def middleClick(self, Cam):
        Cam.xshift += mouseX - pmouseX
        Cam.yshift += mouseY - pmouseY
    
    def leftClick(self, Game, Cam, GUI, Map):
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
            self.nodePlaceIndex += 1
            if(self.nodePlaceIndex >= 90):
                self.nodePlaceIndex = 0
        elif(Game.editingPaths):
            x = int(mouseX - Cam.xshift)
            y = int(mouseY - Cam.yshift)
            if(self.makingConnections == False):
                # Path Node editor
                Map.pathNodes.append(Node(x,y,self.currNode))
                self.currNode+=1
            else:
                self.currNode-=1
                Map.pathNodes[self.currNode].app(Map.pathNodes[self.coneNode])
                Map.pathNodes[self.coneNode].app(Map.pathNodes[self.currNode])
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
                    
    def rightClick(self, Game, Cam):
        Game.PT.players[0].ab1select = False
        Game.PT.players[0].ab2select = False
        Game.PT.players[0].pathfindTo(mouseX - Cam.xshift, mouseY - Cam.yshift, Game)
        Game.PT.players[0].target = None
        for i in Game.PT.players:
            if(i == Game.PT.players[0]):
                continue
            if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2 and i.hp > 0):
                Game.PT.players[0].target = i
                return
        for i in Game.ST.structures:
            if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2 and i.hp > 0):
                Game.PT.players[0].target = i
                return
        for i in Game.CT.creep:
            if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2 and i.hp > 0):
                Game.PT.players[0].target = i
                return    
            
    def lockPlayerTarget(self, Game, Cam):
        player = Game.PT.players[0]
        for i in Game.PT.players:
            if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2): #if you clicked on a player
                if i.alliance != player.alliance:
                    player.target = i
                return
        for i in Game.ST.structures:
            if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2):
                if i.alliance != player.alliance:
                    player.target = i
                return
        # for i in Game.CT.creeps:
        #     if(mouseX - Cam.xshift >= i.x - i.wd/2 and mouseX - Cam.xshift <= i.x + i.wd/2 and mouseY - Cam.yshift >= i.y - i.ht/2 and mouseY - Cam.yshift <= i.y + i.ht/2 and i.hp > 0):
        #         if i.alliance != player.alliance:
        #             player.target = i
        #         return
