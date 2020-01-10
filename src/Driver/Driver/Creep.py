from Mob import *

class Creep(Mob, object):
    
    def __init__(self, **kwds):
        super(Creep, self).__init__(type = "creep", **kwds)
        self.startNode = 3
        self.currentNode = self.startNode
        self.NODE_TRAVERSAL_ERROR = 25
     
    def runAI(self, Game, Map):
        self.moveNode(Game, Map)
        self.move(Game)
        
    def moveNode(self, Game, Map):
        if(self.distancePT(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1]) <= self.NODE_TRAVERSAL_ERROR**2):
            if(self.alliance == "a" and self.currentNode < 69):
                self.currentNode += 1
            elif(self.alliance == "b" and self.currentNode < 69):
                self.currentNode -= 1
                
            self.goalX = Map.laneNodes[self.currentNode][0]
            self.goalY = Map.laneNodes[self.currentNode][1]

        self.pathfindTo(self.goalX, self.goalY, Game)
            
    def drawCreep(self):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)        
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
            
