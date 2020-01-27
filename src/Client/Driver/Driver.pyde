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

ip = "127.0.0.1" # Change to Server's IP
MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()
TeamA = Alliance("a")
TeamB = Alliance("b")
Game = GameTracker()
GUI = GUI()
CM = ClientManager()

def setup(): 
    size(1960, 1080, P2D) # P2D uses OpenGL's faster rendering system
    fullScreen() 
    frameRate(30) # Send the initial packets slower to ensure they arrive correctly 
    smooth(3) # Reduce anti-aliasing for better FPS
    Map.loadMap()
    
    # Focuses the Camera on the center of the map while connecting to the server
    Cam.xshift = -1 * 2500 + 1960 / 2
    Cam.yshift = -1 * 2500 + 1080 / 2
        
    # Connect to the server’s IP address and port
    global C
    C = Client(this, ip, 5204); # Web Socket 5204
    CM.connectClient(C)
    
    frameRate(60) # Switch to 60 fps after connecting
    
def draw():
    # Client processes
    if(C.available() > 0):
        if(CM.caughtUp):
            CM.manageInput(C.readString(), Game, Cam, GUI)
        else:
            CM.setUpClient(C.readString(), Game)
        C.clear() # Clears the Client buffer to reduce packet merging
    CM.writeData(C, Game)
        
    background(0)
    
    Game.incTime() # Ensure a smooth timer - Server constantly ensures the Client's timer is correct
    
    KManage.runActions(Cam, Game, Map, MManage) # Keyboard input
    
    for i in Game.PT.players: # Facilitate local level up calculations on client and server side for accurate GUI
        i.checkLevelUp()
    
    # Game.updateGrid(Game, Map) # Server side
    # Game.runDebuffs(Cam) # Server side
    # Game.runProjectiles(Cam, Game) # Server side
    # Game.ST.runTowerActions(Game, Cam) # Server side
    # Game.PT.runPlayerActions(Game, Cam) # Server side
    # Game.PT.updateMoving(Game) # Server side
    
    Cam.updateCam() 
    
    # Drawing processes
    Map.drawMap(Cam)
    Game.ST.drawStructures(Cam) 
    
    # Alliance specific processes
    if(Game.player >= 0 and Game.player <= 4): # Team A
        Game.CT.drawCreep(Cam, TeamA)
        Game.PT.drawPlayers(Cam, TeamA)
        Game.PT.drawProjectiles(Cam, TeamA)
        TeamA.updateVision(Game)
        TeamA.drawVision(Cam)
    elif(Game.player >= 5 and Game.player <= 9): # Team B
        Game.CT.drawCreep(Cam, TeamB)
        Game.PT.drawPlayers(Cam, TeamB)
        Game.PT.drawProjectiles(Cam, TeamB)
        TeamB.updateVision(Game)
        TeamB.drawVision(Cam)
    
    # Map.drawNodes(Game, Cam, MManage) # Developer Server-side only
    GUI.drawGui(Game, Cam)
    
def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
    
def mousePressed():
    if(mouseButton == 37): # Left click
        MManage.leftClick(Game, Cam, GUI, Map)    
    if(mouseButton == 39): # Right click
        MManage.rightClick(Game, Cam, C, CM)

def mouseDragged(): # Used to pan the camera
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
