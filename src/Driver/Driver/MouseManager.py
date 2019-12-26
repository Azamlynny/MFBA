class MouseManager():
    
    def __init__(self):
        self.player = 1
                
    def middleClick(self, Cam):
        Cam.xshift += mouseX - pmouseX
        Cam.yshift += mouseY - pmouseY
    
    def leftClick(self):
        return
        
    def rightClick(self, Game, Cam):
        Game.PT.players[0].pathfindTo(mouseX - Cam.xshift, mouseY - Cam.yshift, Game)
        Game.PT.players[0].target = None
        for i in Game.PT.players:
            if(i == Game.PT.players[0]):
                continue
            if(mouseX + Cam.xshift >= i.x - i.wd/2 and mouseX + Cam.xshift <= i.x + i.wd/2 and mouseY + Cam.yshift >= i.y - i.ht/2 and mouseY + Cam.yshift <= i.y + i.ht/2):
                Game.PT.players[0].target = i 
