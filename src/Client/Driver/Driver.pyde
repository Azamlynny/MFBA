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

ip = "192.168.2.19" # Change to Server's IP
MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()
TeamA = Alliance("a")
TeamB = Alliance("b")
TeamN = Alliance("c") # Neutral creep
Game = GameTracker()
GUI = GUI()
CM = ClientManager()

def setup(): 
    size(1960, 1080, P2D)
    fullScreen() 
    frameRate(30) # Send the initial packets slower to ensure they arrive correctly 
    smooth(3)
    Map.loadMap()
    
    # Focuses the Camera on the center of the map
    Cam.xshift = -1 * 2500 + 1960 / 2
    Cam.yshift = -1 * 2500 + 1080 / 2
        
    # Connect to the server’s IP address and port
    global C
    C = Client(this, ip, 5204); #Replace with your server’s IP and port
    CM.connectClient(C)
    frameRate(60) # Switch to 60 fps after connecting
    
def draw():
    if(C.available() > 0):
        if(CM.caughtUp):
            CM.manageInput(C.readString(), Game, Cam)
        else:
            CM.setUpClient(C.readString(), Game)
        C.clear()
    CM.writeData(C, Game)
        
    background(0)
    Game.incTime()
    KManage.runActions(Cam, Game, Map, MManage)
    Cam.updateCam()
    Map.drawMap(Cam)
    Game.updateGrid(Game, Map)
    # Game.runDebuffs(Cam) # Server side
    Game.runProjectiles(Cam, Game)
    Game.ST.drawStructures(Cam)
    
    for i in Game.PT.players: # Facilitate local level up calculations on client side
        i.checkLevelUp()
    
    # Game.ST.runTowerActions(Game, Cam) # Server side
    # Game.PT.runPlayerActions(Game, Cam) # Server side
    # Game.PT.updateMoving(Game) # Server side
    
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
        Game.PT.drawProjectiles(Cam, TeamA)
        TeamB.updateVision(Game)
        TeamB.drawVision(Cam)
    
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
        MManage.rightClick(Game, Cam, C, CM)

def mouseDragged(): 
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
