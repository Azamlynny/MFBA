from Player import * 

class PlayerTracker():

    def __init__(self):
        self.players = []
        self.players.append(Player(xPos = 50, yPos = 50, wd = 50, ht = 50, strength = 5, speed = 6, hp = 250, hpMax = 250, hpRegen = 1.5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 1000, alliance = "a", visionRange = 500))
        self.players.append(Player(xPos = 500, yPos = 200, wd = 70, ht = 70, strength = 5, speed = 3, hp = 250, hpMax = 250, hpRegen = 5, atk = 20, atkSpeed = 1.0, armor = 3, atkRange = 100, alliance = "b", visionRange = 500))        
        
    def drawPlayers(self, Alliance):
        scale = 5000 / Alliance.resolution
        for i in self.players:
            if(Alliance.vision[int(i.x / scale)][int(i.y / scale)]):
                i.drawPlayer()
                i.drawHealth()
                
    def runPlayerActions(self, Game):
        for i in self.players:
            i.defaultAttack(Game)
            
    def updateMoving(self, Game):
        for i in self.players:
            i.move(Game)
