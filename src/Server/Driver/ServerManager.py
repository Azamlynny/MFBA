add_library('net')

class ServerManager():
    
    def __init__(self):
        self.IP = None
        
    def sendData(self, S, Game):
        S.write("game_time " + str(Game.time) + " \n")
