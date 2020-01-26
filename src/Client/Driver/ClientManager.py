add_library('net')

from Util import *

class ClientManager():
    
    def __init__(self):
        self.caughtUp = False
        self.IP = None
        self.hasPlayerID = False
        
    def connectClient(self, C):
        self.IP = str(C.ip())
        C.write("CIP" + " " + str(C.ip()))
        print("My IP: " + C.ip())
    
    def setUpClient(self, input, Game):
        
        self.caughtUp = True
    
    def manageInput(self, input, Game, Cam):
        p = Game.player
        
        # Converts white space seperated input into an array
        input = input.split("\n")
        input = input[0].encode('utf8').split(' ')
                    
        if("start" in input):
            a = input.index("start")
            b = input.index("end")
            input = input[a+1:b]
        
        print(input)
        
        if(self.hasPlayerID == False):
            if(str(input[0]) == self.IP and is_int(input[1])):
                Game.player = int(input[1])
                print("Player " + str(Game.player))
                self.hasPlayerID = True
                Cam.xshift = -1 * Game.PT.players[Game.player].x + 1960/2
                Cam.yshift = -1 * Game.PT.players[Game.player].y + 1080/2
        else:
            if("game_time" in input):
                a = input.index("game_time")
                b = input.index("e_game_time")
                game_time = input[a+1:b]
                if(is_int(game_time[0])):
                    Game.time = int(game_time[0])
            
            if("player_pos" in input):
                a = input.index("player_pos")
                b = input.index("e_player_pos")
                player_pos = input[a+1:b]
                for i in range(0,10):
                    Game.PT.players[i].x = int(player_pos[i * 2])
                    Game.PT.players[i].y = int(player_pos[i * 2 + 1])
            
            if("player_hp" in input):
                a = input.index("player_hp")
                b = input.index("e_player_hp")
                player_hp = input[a+1:b]
                for i in range(0,10):
                    Game.PT.players[i].hp = int(player_hp[i])
                    
            if("structure_hp" in input):
                a = input.index("structure_hp")
                b = input.index("e_structure_hp")
                structure_hp = input[a+1:b]
                for i in range(0,18):
                    Game.ST.structures[i].hp = int(structure_hp[i])
            
    def writeData(self, C, Game):        
        p = Game.player
        
        if(self.hasPlayerID == False):
            C.write("reqPlayerID" + " " + self.IP)
        else:
            if(p != None):
                return
                # C.write("player " + str(C.ip()) + " " + str(int(Game.PT.players[p].x)) + " " + str(int(Game.PT.players[p].y)))
                # print("player " + str(int(Game.PT.players[0].x)) + " " + str(int(Game.PT.players[0].y)))
