from Entity import *
from KeyManager import *
from MouseManager import *
from Camera import *
from Map import * 


MManage = MouseManager()
KManage = KeyManager()
Cam = Camera(0,0)
Map = Map()

def setup():
    frameRate(60)
    size(1960, 1080)
    fullScreen()

def draw():
    KManage.runActions(Cam)
    Cam.updateCam()
    Map.drawMap()
    fill(0)
    

def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
    
    
def mouseClicked():
    if(mouseButton == 37): # Left click
        MManage.leftClick()    
    if(mouseButton == 39): # Right click
        MManage.rightClick()

def mouseDragged(): 
    if(mouseButton == 3): # Middle click
        MManage.middleClick(Cam)
