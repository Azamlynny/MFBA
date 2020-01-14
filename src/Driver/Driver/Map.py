from Tree import *
from Util import *
from Node import *

class Map():
    
    def __init__(self):
        self.objects = []
        self.laneNodesNum = 70
        self.laneNodes = [[0 for i in range(2)] for j in range(self.laneNodesNum)] 
        self.pathNodesNum = 200
        self.pathNodes = []
        
    def loadMap(self, MouseManager):
        print("Loading Map")
        fin = open("map.txt", 'r')
        for aline in fin:
            values = aline.split()
            self.objects.append(Tree(xPos = int(values[0]), yPos = int(values[1]), treeType = int(values[2])))
        self.img = loadImage("MFBAMap.png")
        fin.close()
        print("Map Loaded")
        
        print("Loading Nodes")
        fin = open("lane_nodes.txt", 'r')
        count = 0
        for aline in fin:
            values = aline.split()
            self.laneNodes[count][0] = int(values[0])
            self.laneNodes[count][1] = int(values[1])
            count+=1
        fin.close()
        print("Nodes Loaded")
        
        print("Loading Paths")
        fin = open("path_nodes.txt", 'r')
        for aline in fin:
            values = aline.split()
            n = Node(int(values[0]), int(values[1]), int(values[2]))
            self.pathNodes.append(n)
            for i in range(3, len(values)):
                n = Node(0,0,int(values[i]))
                self.pathNodes[int(values[2])].app(n)
            last = int(values[2])
        MouseManager.currNode = last + 1
        fin.close()
        print("Paths Loaded")
        
    def drawMap(self, Cam):
        fill(245)
        rect(0,0,5000,5000)
        image(self.img, 0,0, 5000, 5000)
        for i in self.objects:
            if(sd(Cam, i.x,i.y,i.wd,i.ht)):
                i.drawTree()
    
    def drawNodes(self, Game, Cam, MouseManager):
        if(Game.editingNodes):
            count = 0
            for i in self.laneNodes:
                fill(255)
                ellipse(i[0],i[1],30,30)
                fill(0)
                text(count, i[0], i[1])
                count += 1
            fill(255)
            text(MouseManager.nodePlaceIndex, 50-Cam.xshift, 50-Cam.yshift)
    
    def drawPaths(self, Game, Cam, MouseManager, Map):
        if(Game.editingPaths):
            for i in self.pathNodes:
                i.drawNode(Map)
            fill(255)
            text(MouseManager.currNode, 25-Cam.xshift, 25-Cam.yshift)
            text(MouseManager.coneNode, 25-Cam.xshift, 50-Cam.yshift)
            text(MouseManager.makingConnections, 25-Cam.xshift, 75-Cam.yshift)
