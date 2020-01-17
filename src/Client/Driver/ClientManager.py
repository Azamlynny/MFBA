add_library('net')

class ClientManager():
    
    def __init__(self):
        self.caughtUp = False
        
    def setUpClient(self, input, Game):
        self.caughtUp = True
    
    def manageInput(self, input, Game):
        
        # Converts white space seperated input into an array
        input = input.split("\n")
        input = input[0].encode('utf8').split(' ')
        
        if(input[0] == "game_time"):
            Game.time = int(input[1])
            
    def writeData(self, C, Game):
        C.write("player0 " + str(int(Game.PT.players[0].x)) + " " + str(int(Game.PT.players[0].y)))
        # print("player0 " + str(int(Game.PT.players[0].x)) + " " + str(int(Game.PT.players[0].y)))
