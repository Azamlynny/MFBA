class MouseManager():
    
    def __init__(self):
        self.player = 1
                
    def middleClick(self, Cam):
        Cam.xshift += mouseX - pmouseX
        Cam.yshift += mouseY - pmouseY
    
    def leftClick(self):
        print("temp")
        
    def rightClick(self, Game, Cam):
        Game.PT.players[0].pathfindTo(mouseX - Cam.xshift, mouseY - Cam.yshift)
        Game.PT.players[0].target = None
        for i in Game.PT.players:
            if(i == Game.PT.players[0]):
                continue
            if(i.distancePT(mouseX + Cam.xshift, mouseY + Cam.yshift) <= i.atkRange):
                Game.PT.players[0].target = i 
