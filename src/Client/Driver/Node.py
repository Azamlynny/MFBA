import math

class Node:

    def __init__(self, xPos, yPos, num):
        self.x = xPos
        self.y = yPos
        self.name = num
        self.adj = []
        
        # Pathfinding 
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0
    
    def app(self, Node): # Append a node
        self.adj.append(Node.name)    
    
    def distancePT(self, x, y): 
        """Find the distance between an object and a point"""
        return Math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def drawNode(self, Map):
        """Draw nodes, should only be active for developer mode"""
        fill(255)
        ellipse(self.x, self.y, 25, 25)
        fill(0)
        text(self.name, self.x, self.y)
        self.drawConnections(Map)
        
    def drawConnections(self, Map):
        stroke(255,50)
        strokeWeight(4)
        for i in self.adj:
            for o in Map.pathNodes:
                if(o.name == i):
                    line(self.x, self.y, o.x, o.y)
        noStroke()
    
