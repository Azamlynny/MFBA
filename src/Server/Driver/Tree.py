from Entity import *

class Tree(Entity, object):

    def __init__(self, treeType, **kwds): #TODO: add debuffs
        super(Tree, self).__init__(wd = 75, ht = 75, **kwds)
        self.treeType = treeType
        
    def drawTree(self):
        if(self.treeType == 0):
            fill(40,140,70)
        elif(self.treeType == 1):
            fill(86,127,33)
        elif(self.treeType == 2):
            fill(93,155,13)
        elif(self.treeType == 3):
            fill(32,108,8)
        elif(self.treeType == 4):
            fill(90,169,66)
            
        rect(self.x-self.wd/2, self.y-self.ht/2, self.wd, self.ht)
    
