add_library('net')
from Entity import *
from KeyManager import *
from MouseManager import *
from Camera import *
from Map import * 
from Alliance import *
from GameTracker import *

MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()
TeamA = Alliance("A")
TeamB = Alliance("B")
TeamN = Alliance("N") # Neutral creep
Game = GameTracker()

def setup():
    frameRate(60)
    size(1960, 1080)
    fullScreen()

def draw():
    Game.incTime()
    KManage.runActions(Cam, Game)
    Cam.updateCam()
    Map.drawMap()
    Game.updateGrid(Game.PT, Map)
    Game.runDebuffs()
    Game.runProjectiles(Game)
    Game.PT.runPlayerActions(Game)
    Game.PT.updateMoving(Game)
    Game.PT.drawPlayers(TeamA)
    fill(0)
    rect(500,500,200,200)
    
    TeamA.updateVision(Game)
    TeamA.drawVision()

def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
    
    
def mousePressed():
    if(mouseButton == 37): # Left click
        MManage.leftClick(Game, Cam)    
    if(mouseButton == 39): # Right click
        MManage.rightClick(Game, Cam)

def mouseDragged(): 
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
