from Player import *
import datetime

class GUI():
    
    def __init__(self):
        self.playerSlot = 0
        self.type = "player"
        
    def drawGui(self, Game, Cam):
        """Draw GUI and various aspects like abilities, etc."""
        if(not Cam.spectatorMode):
            fill(103, 108, 126, 200)
            x = -Cam.xshift + 430 # Top left corner of the GUI panel
            y = -Cam.yshift + 930
            w = 1100
            h = 150
            
            # Allows for viewing attributes of any Attackable
            if(self.type == "player"):
                p1 = Game.PT.players[self.playerSlot]
            elif(self.type == "structure"):
                p1 = Game.ST.structures[self.playerSlot]
            elif(self.type == "creep"):
                p1 = Game.CT.creep[self.playerSlot]
            else:
                p1 = Game.PT.players[0]
    
            rect(x,y, w, h) # GUI panel
    
            # Game Time bar
            gtbx = -Cam.xshift + width/2
            gtby = -Cam.yshift
            quad(gtbx - 75, gtby, gtbx + 75, gtby, gtbx + 55, gtby+55,  gtbx - 55, gtby+55)
            
            # Game Time text
            fill(255)
            textSize(20)
            time = datetime.timedelta(seconds = Game.time)
            text(str(time), gtbx, gtby + 35)
            
            # Health bar background
            fill(0,0,0)
            rect(x + 250, y + 70, 600, 50, 5, 5, 5, 5)
            # Health bar foreground
            fill(0,204,20)
            if(p1.hp >= 0):
                rect(x + 250, y + 70, round(600 * p1.hp/p1.hpMax), 50, 5, 5, 5, 5)
            
            if(self.type == "player"):        
                # Experience bar background 
                fill(0,0,0, 100)
                rect(x + 25, y + 70, 200, 50, 5, 5, 5, 5)
                # Experience bar foreground 
                fill(255, 190, 0)
                if(p1.lvl < 25):
                    rect(x + 25, y + 70, round(200 * p1.xp/xpToLevel[p1.lvl]), 50, 5, 5, 5, 5)
                else:
                    rect(x + 25, y + 70, 200, 50, 5, 5, 5, 5)
            
            # Ability bar background                                
            fill(0,0,0, 50)
            rect(x + 850 + 20, y + 35, 100, 100)
            rect(x + 850 + 130, y + 35, 100, 100)
            
            if(self.type == "player"): # Only players have ability cooldowns       
                # Ability bar foreground
                fill(0,0,0,150)
                index = -1
                for i in range(0,len(Game.PT.players[self.playerSlot].debuffs)):
                    if(Game.PT.players[self.playerSlot].debuffs[i].debuff == "ab1cd"):
                        index = int(i)
                        break
                if(index != -1):
                    rect(x + 850 + 20, y + 35, 100, int((100 * (float(p1.debuffs[index].time) / p1.ab1cooldown))) + 1)
                
                index = -1
                for i in range(0,len(Game.PT.players[self.playerSlot].debuffs)):
                    if(Game.PT.players[self.playerSlot].debuffs[i].debuff == "ab2cd"):
                        index = int(i)
                        break
                if(index != -1):
                    rect(x + 850 + 130, y + 35, 100, int((100 * (float(p1.debuffs[index].time) / p1.ab2cooldown))) + 1)    
                    
            textAlign(CENTER)
            fill(255)
            
            # Teacher name
            textSize(40)
            text(p1.name, x + w/2, y + 45)
            
            # Health bar text
            textSize(25)
            text(str(int(p1.hp)) + "/" + str(p1.hpMax), x + 550, y + 105)
            
            # Experience bar text
            if(self.type == "player"):
                text("Level " + str(p1.lvl), x + 125, y + 105)
            
            # Ability name text
            textSize(12)
            text(p1.ab1name, x + 850 + 20 + 50, y + 30)
            text(p1.ab2name, x + 850 + 130 + 50, y + 30)
            
            # Frames per second
            textSize(12)
            fill(0,0,0, 100)
            text(int(frameRate), 10 - Cam.xshift, 10 - Cam.yshift)
            
            # End of game message
            if Game.winner != None:
                textSize(128)
                textAlign(CENTER, CENTER)
                if Game.winner == "a":
                    fill(0, 0, 255)
                    text("Blue Alliance Wins", x+540, y-480)
                if Game.winner == "b":
                    fill(255, 0, 0)
                    text("Red Alliance Wins", x+540, y-480)
