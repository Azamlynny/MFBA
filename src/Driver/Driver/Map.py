from Tree import *

class Map():
    
    def __init__(self):
        self.objects = []
        #self.objects.append(Tree(xPos = 80, yPos = 800))
        
    def loadMap(self):
        print("Loading Map")
        fin = open("map.txt", 'r')
        for aline in fin:
            values = aline.split()
            self.objects.append(Tree(xPos = int(values[0]), yPos = int(values[1]), treeType = int(values[2])))
        # self.img = loadImage("MFBAMap.png")
        print("Map Loaded")
        
    def drawMap(self):
        fill(245)
        rect(0,0,5000,5000)
        # image(self.img, 0,0, 5000, 5000)
        for i in self.objects:
            i.drawTree()
        
        
