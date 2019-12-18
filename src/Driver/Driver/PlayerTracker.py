from Player import * 

class PlayerTracker():

    def __init__(self):
        self.players = []
        self.players.append(Player(xPos = 50, yPos = 50, strength = 5, speed = 100, hp = 250, hpRegen = 1.5, atk = 10, armor = 3, atkRange = 100, alliance = "a", visionRange = 500))
        
    def drawPlayers(self):
        for i in self.players:
            i.drawPlayer();
