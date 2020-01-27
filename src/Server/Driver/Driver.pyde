add_library('net') # Imports processing Network library

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
TeamA = Alliance("a")
TeamB = Alliance("b")
Game = GameTracker()
GUI = GUI()
SM = ServerManager()

def setup():
    frameRate(60)
    size(1960, 1080, P2D) # P2D uses OpenGL's faster rendering system
    smooth(3) # Reduce anti-aliasing for better FPS
    fullScreen()
    Map.loadMap()
    
    # Focuses the Camera on the player
    Cam.xshift = -1 * Game.PT.players[0].x + 1960/2
    Cam.yshift = -1 * Game.PT.players[0].y + 1080/2
    
    global S # Server
    S = Server(this, 5204) # Web Socket 5204
    SM.IP = S.ip()
    print("Server IPv4 Address")
    print(S.ip())
    
def draw():
    # Server processes
    global S # Server
    
    C = S.available() 
    SM.connectingClient = False
    if(C != None): # If there is data from the clients
        SM.readData(S, C, Game, MManage)
    SM.sendData(S, Game)
    
    if(Cam.spectatorMode):
        scale(0.22) # Zoom out for spectator mode
    else:
        scale(1)
    
    background(0)
    
    # Drawing processees
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

def mouseDragged(): # Used to pan the camera
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
        
