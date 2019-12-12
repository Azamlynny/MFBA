class MouseManager():
    
    def __init__(self):
        self.player = 1
                
    def middleClick(self, Cam):
        Cam.xshift += mouseX - pmouseX
        Cam.yshift += mouseY - pmouseY
    
    def leftClick(self):
        print("temp")
        
    def rightClick(self):
        print("temp")
