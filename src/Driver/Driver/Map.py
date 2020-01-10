from Tree import *
from Util import *

class Map():
    
    def __init__(self):
        self.objects = []
        self.laneNodesNum = 90
        self.laneNodes = [[0 for i in range(2)] for j in range(self.laneNodesNum)] 
        #print(self.laneNodes[80][1])
        #self.objects.append(Tree(xPos = 80, yPos = 800))
        
    def loadMap(self):
        print("Loading Map")
        fin = open("map.txt", 'r')
        for aline in fin:
            values = aline.split()
            self.objects.append(Tree(xPos = int(values[0]), yPos = int(values[1]), treeType = int(values[2])))
        self.img = loadImage("MFBAMap.png")
        print("Map Loaded")
        
        print("Loading Nodes")
        fin = open("lane_nodes.txt", 'r')
        count = 0
        for aline in fin:
            values = aline.split()
            self.laneNodes[count][0] = int(values[0])
            self.laneNodes[count][1] = int(values[1])
            count+=1
        print("Nodes Loaded")
        
    def drawMap(self, Cam):
        fill(245)
        rect(0,0,5000,5000)
        image(self.img, 0,0, 5000, 5000)
        for i in self.objects:
            if(sd(Cam, i.x,i.y,i.wd,i.ht)):
                i.drawTree()
    
    def drawNodes(self, Game, Cam):
        if(Game.editingNodes):
            fill(255)
            for i in self.laneNodes:
                ellipse(i[0],i[1],30,30)
        
