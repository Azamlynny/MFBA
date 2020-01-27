from Mob import *

class Creep(Mob, object):
    
    def __init__(self, startNode, **kwds):
        super(Creep, self).__init__(type = "creep", strength = 5, speed = 4, hp = 100, hpMax = 100, hpRegen = 0.5, atk = 5, atkSpeed = 1.0, armor = 3, **kwds)
        self.startNode = startNode
        self.currentNode = self.startNode
        self.NODE_TRAVERSAL_ERROR = 25
        self.AGRO_RANGE = 300
        self.name = "Creep"
        self.type = "creep"

    def runAI(self, Game, Map):
        """Run Creep pathfinding and target selection"""
        self.checkAgro(Game, Map)
        if(self.target == None):
            self.moveNode(Game, Map)
            self.pathfindTo(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1], Game)
            self.move(Game)
        else:
            self.pathfindTo(self.target.x, self.target.y, Game)
            self.move(Game)
            self.defaultAttack(Game)
            if(self.target == None or self.target.hp <= 0): # Creep/Tower/Player killed
                self.Target = None
                self.atkCooldown = 0
                self.pathfindTo(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1], Game)
        
    def moveNode(self, Game, Map):
        """Set target node for pathfinding"""
        if(self.distancePT(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1]) <= self.NODE_TRAVERSAL_ERROR**2):
            if(self.alliance == "a" and self.currentNode < 69):
                self.currentNode += 1
            elif(self.alliance == "b" and self.currentNode < 69):
                self.currentNode -= 1
            
    def drawCreep(self):
        """Draw Creep"""
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)        
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        
    def checkAgro(self, Game, Map):
        """Select target for creeps"""
        if(self.target != None):
            if(self.distance(self.target) > self.AGRO_RANGE ** 2):
                self.target = None
                self.atkCooldown = 0
                self.pathfindTo(Map.laneNodes[self.currentNode][0], Map.laneNodes[self.currentNode][1], Game)
                return
        
        if(self.target == None):
            self.atkCooldown = 0
            for i in Game.CT.creep:
                if(i.alliance != self.alliance and i.hp > 0):
                    if(self.distance(i) <= self.AGRO_RANGE ** 2):
                        self.target = i
                        return
            for i in Game.PT.players:
                if(i.alliance != self.alliance and i.hp > 0):
                    if(self.distance(i) <= self.AGRO_RANGE ** 2):
                        self.target = i
                        return
            for i in Game.ST.structures:
                if(i.alliance != self.alliance and i.hp > 0):
                    if(self.distance(i) <= self.AGRO_RANGE ** 2):
                        self.target = i
                        return
                    
                
