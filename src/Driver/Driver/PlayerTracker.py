from Player import * 

class PlayerTracker():

    def __init__(self):
        self.players = []
        self.players.append(Player(xPos = 50, yPos = 50, strength = 5, speed = 100, hp = 250, hpMax = 250, hpRegen = 1.5, atk = 10, armor = 3, atkRange = 100, alliance = "a", visionRange = 500))
        self.players.append(Player(xPos = 1000, yPos = 1000, strength = 5, speed = 100, hp = 250, hpMax = 250, hpRegen = 1.5, atk = 10, armor = 3, atkRange = 100, alliance = "b", visionRange = 500))        
        
    def drawPlayers(self, Alliance):
        scale = 10000 / Alliance.resolution
        for i in self.players:
            if(Alliance.vision[i.x / scale][i.y / scale]):
                i.drawPlayer()
                i.drawHealth()
                
    def runPlayerActions(self, Game):
        for i in self.players:
            i.defaultAttack(Game)
        
