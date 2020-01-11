from Creep import * 
from Util import *

class CreepTracker():

    def __init__(self):
        self.creep = []
             
    def drawCreep(self, Cam, Alliance):
        scale = 5000 / Alliance.resolution
        for i in self.players:
            if(sd(Cam,i.x,i.y,i.wd,i.ht)):
                if(Alliance.vision[int(i.x / scale)][int(i.y / scale)]):
                    if any(j.debuff == "dead" for j in i.debuffs):
                        pass
                    else:
                        i.drawCreep()
                        i.drawHealth()
                
    def runPlayerActions(self, Game, Cam):
        for i in self.players:
            i.defaultAttack(Game)
            i.checkHealth(Game, Cam)
    def updateMoving(self, Game):
        for i in self.players:
            i.move(Game)
