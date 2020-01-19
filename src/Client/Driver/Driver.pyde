add_library('net')

from Entity import *
from KeyManager import *
from MouseManager import *
from Camera import *
from Map import * 
from Alliance import *
from GameTracker import *
from GUI import *
from StructureTracker import *
from Creep import *
from ClientManager import *

MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()
TeamA = Alliance("A")
TeamB = Alliance("B")
TeamN = Alliance("N") # Neutral creep
Game = GameTracker()
GUI = GUI()
CM = ClientManager()

def setup(): 
    frameRate(30) # Send the initial packets slower to ensure they arrive correctly 
    size(1960, 1080, P2D)
    smooth(3)
    fullScreen()
    Map.loadMap()
    
    # Focuses the Camera on the player
    Cam.xshift = -1 * Game.PT.players[0].x + 1960/2
    Cam.yshift = -1 * Game.PT.players[0].y + 1080/2
    
    # Connect to the server’s IP address and port
    global C
    C = Client(this, "192.168.2.19", 5204); #Replace with your server’s IP and port
    CM.connectClient(C)
    frameRate(60) # Switch to 60 fps after connecting
    
def draw():
    if(C.available() > 0):
        if(CM.caughtUp):
            CM.manageInput(C.readString(), Game)
        else:
            CM.setUpClient(C.readString(), Game)
    CM.writeData(C, Game)
        
    background(0)
    Game.incTime()
    KManage.runActions(Cam, Game, Map, MManage)
    Cam.updateCam()
    Map.drawMap(Cam)
    Game.updateGrid(Game, Map)
    Game.runDebuffs(Cam)
    Game.runProjectiles(Cam, Game)
    Game.ST.drawStructures(Cam)
    Game.ST.runTowerActions(Game)
    Game.CT.drawCreep(Cam, TeamA)
    Game.PT.runPlayerActions(Game, Cam)
    Game.PT.updateMoving(Game)
    Game.PT.drawPlayers(Cam, TeamA)
    TeamA.updateVision(Game)
    TeamA.drawVision(Cam)
    Map.drawNodes(Game, Cam, MManage)
    GUI.drawGui(Game, Cam)
    
    
def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
    
    
def mousePressed():
    if(mouseButton == 37): # Left click
        MManage.leftClick(Game, Cam, GUI, Map)    
    if(mouseButton == 39): # Right click
        MManage.rightClick(Game, Cam)

def mouseDragged(): 
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
