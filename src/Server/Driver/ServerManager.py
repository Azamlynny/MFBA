add_library('net')

from Util import *

class ServerManager():
    
    def __init__(self):
        self.IP = None
        self.clients = []
        # self.clients.append("placeholder") # Placeholder client for dev testing
        
    def sendData(self, S, Game):
        S.write("game_time " + str(Game.time) + " \n")
        
    def readData(self, S, C, Game):
        input = C.readString()
        input = input.split('\n')
        input = input[0].encode('utf8').split(' ')

        if(input[0] == "CIP"): # New Client IP connecting
            self.clients.append(str(input[1]))
            print("New Client at " + str(input[1]))
            # Tell the new client their player ID
            S.write(str(input[1]) + " " + str(len(self.clients) - 1))
        
        if(input[0] == "reqPlayerID"): # Requesting player ID
            S.write(str(input[1]) + " " + str(len(self.clients) - 1))
            # Sends IP and plyer ID

        player = None                
        for i in range (0, len(self.clients)):
            if(self.clients[i] == input[1]):
                player = i
        
        # Server only reads data from clients it can validate        
        if(player != None):        
            if(input[0] == "player"):
                if(is_int(input[2]) and is_int(input[3])):
                    Game.PT.players[player].x = int(input[2])
                    Game.PT.players[player].y = int(input[3])
                
