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
            out = " d d start " # Buffer for packet merges
        
            # Appending game time
            out += "game_time " + str(Game.time) + " e_game_time "
        
            # Appending player position
            temp = "player_pos" + " " + str(int(Game.PT.players[0].x)) + " " + str(int(Game.PT.players[0].y))  + " " + str(int(Game.PT.players[1].x)) + " " + str(int(Game.PT.players[1].y))  + " " + str(int(Game.PT.players[2].x)) + " " + str(int(Game.PT.players[2].y)) + " " + str(int(Game.PT.players[3].x)) + " " + str(int(Game.PT.players[3].y)) + " " + str(int(Game.PT.players[4].x)) + " " + str(int(Game.PT.players[4].y)) + " " + str(int(Game.PT.players[5].x)) + " " + str(int(Game.PT.players[5].y)) + " " + str(int(Game.PT.players[6].x)) + " " + str(int(Game.PT.players[6].y)) + " " + str(int(Game.PT.players[7].x)) + " " + str(int(Game.PT.players[7].y)) + " " + str(int(Game.PT.players[8].x)) + " " + str(int(Game.PT.players[8].y)) + " " + str(int(Game.PT.players[9].x)) + " " + str(int(Game.PT.players[9].y)) + " e_player_pos " 
            
            out += temp
            
            # Appending player health
            temp = "player_hp" + " " + str(int(Game.PT.players[0].hp)) + " " + str(int(Game.PT.players[1].hp)) + " " + str(int(Game.PT.players[2].hp)) + " " + str(int(Game.PT.players[3].hp)) + " " + str(int(Game.PT.players[4].hp)) + " " + str(int(Game.PT.players[5].hp)) + " " + str(int(Game.PT.players[6].hp)) + " " + str(int(Game.PT.players[7].hp)) + " " + str(int(Game.PT.players[8].hp)) + " " + str(int(Game.PT.players[9].hp)) + " e_player_hp " 
            
            out += temp
            
            # Appending structure health
            temp = "structure_hp" + " " + str(int(Game.ST.structures[0].hp)) + " " + str(int(Game.ST.structures[1].hp)) + " " + str(int(Game.ST.structures[2].hp)) + " " + str(int(Game.ST.structures[3].hp)) + " " + str(int(Game.ST.structures[4].hp)) + " " + str(int(Game.ST.structures[5].hp)) + " " + str(int(Game.ST.structures[6].hp)) + " " + str(int(Game.ST.structures[7].hp)) + " " + str(int(Game.ST.structures[8].hp)) + " " + str(int(Game.ST.structures[9].hp)) + " " + str(int(Game.ST.structures[10].hp)) + " " + str(int(Game.ST.structures[11].hp)) + " " + str(int(Game.ST.structures[12].hp)) + " " + str(int(Game.ST.structures[13].hp)) + " " + str(int(Game.ST.structures[14].hp)) + " " + str(int(Game.ST.structures[15].hp)) + " " + str(int(Game.ST.structures[16].hp)) + " " + str(int(Game.ST.structures[17].hp)) + " e_structure_hp "
                
            out += temp
            
            # Appending creep position, health, and alliance
            temp = "creep "

            for i in Game.CT.creep:
                temp += str(int(i.x)) + " " + str(int(i.y)) + " " + str(int(i.hp)) + " " + str(i.alliance) + " "

            temp += "e_creep "

            out += temp
            
            
            # Appending projectiles
            temp = "projectiles " 
            
            for i in Game.PT.players:
                if(i.atkType == "ranged"):
                    for o in i.projectiles:
                        temp += str(int(o.x)) + " " + str(int(o.y)) + " " + str(int(o.wd)) + " "
            for i in Game.CT.creep:
                if(i.atkType == "ranged"):
                    for o in i.projectiles:
                        temp += str(int(o.x)) + " " + str(int(o.y)) + " " + str(int(o.wd)) + " "
            for i in Game.ST.structures:
                if(i.atkType == "ranged"):
                    for o in i.projectiles:
                        temp += str(int(o.x)) + " " + str(int(o.y)) + " " + str(int(o.wd)) + " "
            temp += "e_projectiles "

            out += temp
            
            
            out += "end d d " # Buffer for packet merges

            S.write(out)
            # print(out)
        
    def readData(self, S, C, Game, MManage):
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
            if("mouse_in" in input):
                a = input.index("mouse_in")
                b = input.index("e_mouse_in")
                mouse = input[a+1:b]
                # print(mouse[0] + " " + mouse[1] + " " + mouse[2])
                p = int(mouse[0]) # Player number/ID
                x = int(mouse[1])
                y = int(mouse[2])
                MManage.rightClick(Game, p, x, y)
    
