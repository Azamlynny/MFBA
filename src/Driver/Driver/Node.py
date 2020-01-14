import math

class Node:

    def __init__(self, xPos, yPos, num):
        self.x = xPos
        self.y = yPos
        self.name = num
        self.adj = []
    
    def app(self, Node): # Append a node
        self.adj.append(Node.name)    
    
    def distancePT(self, x, y): 
        """Find the distance between an object and a point"""
        return Math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def drawNode(self):
        fill(255)
        ellipse(self.x, self.y, 25, 25)
        fill(0)
        text(self.name, self.x, self.y)
        self.drawConnections()
        
    def drawConnections(self):
        for i in self.adj:
            stroke(255)
            line(self.x, self.y, i.x, i.y)
