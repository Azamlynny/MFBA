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
                        
            
            # if("creep_info" in input):
            #     a = input.index("creep_info")
            #     b = input.index("e_creep_info")
            #     creep = input[a+1:b]
            #     count = 0
            #     if(len(creep) >= 29):
            #         for i in range(0,30,4):
            #             print(str(len(creep)) + " " + str(i) + " " + str(len(Game.CT.creep)) + " " + str(count))
            #             Game.CT.creep[count].y = int(creep[i+1])
            #             Game.CT.creep[count].alliance = str(creep[i+2])
            #             Game.CT.creep[count].hp = int(creep[i+3])
            #             count += 1
            
    def writeData(self, C, Game):        
        p = Game.player
        
        if(self.hasPlayerID == False):
            C.write("reqPlayerID" + " " + self.IP)
        else:
            if(p != None):
                return
                # C.write("player " + str(C.ip()) + " " + str(int(Game.PT.players[p].x)) + " " + str(int(Game.PT.players[p].y)))
                # print("player " + str(int(Game.PT.players[0].x)) + " " + str(int(Game.PT.players[0].y)))
