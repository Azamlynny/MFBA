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
from ServerManager import *

MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()
TeamA = Alliance("A")
TeamB = Alliance("B")
TeamN = Alliance("N") # Neutral creep
Game = GameTracker()
GUI = GUI()
SM = ServerManager()

def setup():
    frameRate(60)
    size(1960, 1080, P2D)
    smooth(3)
    fullScreen()
    Map.loadMap()
    
    # Focuses the Camera on the player
    Cam.xshift = -1 * Game.PT.players[0].x + 1960/2
    Cam.yshift = -1 * Game.PT.players[0].y + 1080/2
    global S # Server
    S = Server(this, 5204)
    SM.IP = S.ip()
    print("Server IP4v Address")
    print(S.ip())
    
def draw():
    global S # Server
    
    C = S.available()
    SM.connectingClient = False 
    if(C != None):
        SM.readData(S, C, Game, MManage)
        
    SM.sendData(S, Game)
    
    background(0)
    
    # Still used by the server for developer and spectator modes
    KManage.runActions(Cam, Game, Map, MManage) 
    Cam.updateCam()
    Map.drawMap(Cam)
    Game.ST.drawStructures(Cam)
    Game.CT.drawCreep(Cam, TeamA)
    Game.PT.drawPlayers(Cam, TeamA)
    Map.drawNodes(Game, Cam, MManage) # Only draws when in developer mode
    GUI.drawGui(Game, Cam)

    # Game calculations sent to clients
    Game.incTime()
    Game.runDebuffs(Cam)
    Game.updateGrid(Game, Map)
    Game.runProjectiles(Cam, Game)
    Game.ST.runTowerActions(Game, Cam)
    Game.CT.runCreepActions(Game, Map, GUI)
    Game.PT.runPlayerActions(Game, Cam)
    Game.PT.updateMoving(Game)
    
def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
    
    
def mousePressed():
    if(mouseButton == 37): # Left click
        MManage.leftClick(Game, Cam, GUI, Map)
   
    # The server does not control a player but can still spectate GUI and scroll around the map 
    # if(mouseButton == 39): # Right click
    #     MManage.rightClick(Game, Cam)

def mouseDragged(): 
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
        
