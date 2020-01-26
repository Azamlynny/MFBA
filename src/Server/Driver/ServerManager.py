add_library('net')

from Util import *

class ServerManager():
    
    def __init__(self):
        self.IP = None
        self.clients = []
        # self.clients.append("placeholder") # Placeholder client for dev testing
        self.connectingClient = False
        
    def sendData(self, S, Game):
        # print(self.connectingClient)
        if(not self.connectingClient):
            # Appending game time
            out = " d d start "
        
            out += "game_time " + str(Game.time) + " e_game_time "
        
            temp = "player_pos" + " " + str(Game.PT.players[0].x) + " " + str(Game.PT.players[0].y) + " " + str(Game.PT.players[1].x) + " " + str(Game.PT.players[1].y) + " " + str(Game.PT.players[2].x) + " " + str(Game.PT.players[2].y) + " " + str(Game.PT.players[3].x) + " " + str(Game.PT.players[3].y) + " " + str(Game.PT.players[4].x) + " " + str(Game.PT.players[4].y) + " " + str(Game.PT.players[5].x) + " " + str(Game.PT.players[5].y) + " " + str(Game.PT.players[6].x) + " " + str(Game.PT.players[6].y) + " " + str(Game.PT.players[7].x) + " " + str(Game.PT.players[7].y) + " " + str(Game.PT.players[8].x) + " " + str(Game.PT.players[8].y) + " " + str(Game.PT.players[9].x) + " " + str(Game.PT.players[9].y) + " e_player_pos " 
            
            out += temp
            
            temp = "player_hp" + " " + str(Game.PT.players[0].hp) + " " + str(Game.PT.players[1].hp) + " " + str(Game.PT.players[2].hp) + " " + str(Game.PT.players[3].hp) + " " + str(Game.PT.players[4].hp) + " " + str(Game.PT.players[5].hp) + " " + str(Game.PT.players[6].hp) + " " + str(Game.PT.players[7].hp) + " " + str(Game.PT.players[8].hp) + " " + str(Game.PT.players[9].hp) + " e_player_hp " 
            
            out += temp
                    
            temp = "structure_hp" + " " + str(Game.ST.structures[0].hp) + " " + str(Game.ST.structures[1].hp) + " " + str(Game.ST.structures[2].hp) + " " + str(Game.ST.structures[3].hp) + " " + str(Game.ST.structures[4].hp) + " " + str(Game.ST.structures[5].hp) + " " + str(Game.ST.structures[6].hp) + " " + str(Game.ST.structures[7].hp) + " " + str(Game.ST.structures[8].hp) + " " + str(Game.ST.structures[9].hp) + " " + str(Game.ST.structures[10].hp) + " " + str(Game.ST.structures[11].hp) + " " + str(Game.ST.structures[12].hp) + " " + str(Game.ST.structures[13].hp) + " " + str(Game.ST.structures[14].hp) + " " + str(Game.ST.structures[15].hp) + " " + str(Game.ST.structures[16].hp) + " " + str(Game.ST.structures[17].hp) + " e_structure_hp "
                
            out += temp
            
            out += "end d d "
            
            S.write(out)
            # print(out)
        
    def readData(self, S, C, Game):
        input = C.readString()
        input = input.split('\n')
        input = input[0].encode('utf8').split(' ')

        if(input[0] == "CIP"): # New Client IP connecting
            # print("CIP") # Debugging
            self.clients.append(str(input[1]))
            print("New Client at " + str(input[1]))
            # Tell the new client their player ID
            S.write(" d d start " + str(input[1]) + " " + str(len(self.clients) - 1) + " end d d ")
            self.connectingClient = True
        
        if(input[0] == "reqPlayerID"): # Requesting player ID
            # print("req") # Debugging
            S.write(" d d start " + str(input[1]) + " " + str(len(self.clients) - 1) + " end d d ")
            # Sends IP and plyer ID
            self.connectingClient = True

        player = None                
        for i in range (0, len(self.clients)):
            if(self.clients[i] == input[1]):
                player = i
        
        # Server only reads data from clients it can validate        
        if(player != -1):        
            if(input[0] == "player"):
                if(is_int(input[2]) and is_int(input[3])):
                    Game.PT.players[player].x = int(input[2])
                    Game.PT.players[player].y = int(input[3])
    
