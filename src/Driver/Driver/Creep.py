from Mob import *

class Creep(Mob, object):
    
    def __init__(self, startNode, **kwds):
        super(Creep, self).__init__(type = "creep", **kwds)
        self.startNode = startNode
        self.currentNode = self.startNode
        self.NODE_TRAVERSAL_ERROR = 25
        self.AGRO_RANGE = 300

    def runAI(self, Game, Map):
        self.checkAgro(Game, Map)
        if(self.target == None):
            self.moveNode(Game, Map)
            self.pathfindTo(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1], Game)
            self.move(Game)
        else:
            self.pathfindTo(self.target.x, self.target.y, Game)
            self.move(Game)
            self.defaultAttack(Game)
        
    def moveNode(self, Game, Map):
        if(self.distancePT(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1]) <= self.NODE_TRAVERSAL_ERROR**2):
            if(self.alliance == "a" and self.currentNode < 69):
                self.currentNode += 1
            elif(self.alliance == "b" and self.currentNode < 69):
                self.currentNode -= 1
            
    def drawCreep(self):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)        
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        
    def checkAgro(self, Game, Map):
        # if(self.target != None): # To return to the previous node when the player takes the creep out of the lane
        #     hadTarget = True
        # else:
        #     hadTarget = False
        if(self.target != None):
            if(self.distance(self.target) > self.AGRO_RANGE ** 2):
                self.target = None
                self.atkCooldown = 0
                self.pathfindTo(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1], Game)
                return
        
        if(self.target == None):
            for i in Game.PT.players:
                if(self.distance(i) <= self.AGRO_RANGE ** 2):
                    print(i)
                    self.target = i
                
