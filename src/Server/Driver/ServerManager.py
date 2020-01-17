add_library('net')

from Util import *

class ServerManager():
    
    def __init__(self):
        self.IP = None
        
    def sendData(self, S, Game):
        S.write("game_time " + str(Game.time) + " \n")
        
    def readData(self, C, Game):
        input = C.readString()
        input = input.split('\n')
        input = input[0].encode('utf8').split(' ')

        if(input[0] == "player0"):
            # print(input[1] + " " + input[2])
            if(is_int(input[1]) and is_int(input[2])):
                # print("true")
                Game.PT.players[0].x = int(input[1])
                Game.PT.players[0].y = int(input[2])
                
