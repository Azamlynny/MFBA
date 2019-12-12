from Entity import *
from KeyManager import *
from Camera import *
from Map import * 

KManage = KeyManager()
Cam = Camera(0,0)
# Map = Map()

def setup():
    size(1960, 1080)
    fullScreen()

def draw():
    KManage.runActions(Cam)
    Cam.updateCam()
    background(255)
    fill(0)
    rect(0,0,500,500)
    rect(1000,1000,30,500)

def keyPressed():
    KManage.keyInput(str(key))
    
def keyReleased():
    KManage.keyRemove(str(key))
