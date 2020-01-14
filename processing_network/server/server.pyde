add_library('net')
c = Client
input = ""
data = []
xPos = float(0)
yPos = float(0)
xVel = float(0)
yVel = float(0)
errorX = float(0)
errorY = float(0)
integralY = float(0)
derivativeY = float(0)
integralX = float(0)
derivativeX = float(0)
error_prevX = float(0)
error_prevY = float(0)
framerate = 60
def PID(xTarget, yTarget):
    kP = 0.1
    kD = 0.01
    global xPos, yPos, xVel, yVel, error_prevY, error_prevX, errorX, errorY, integralX, integralY, derivativeX, derivativeY, error_prevX, error_prevY, framerate
    kI = 0
    dt = float(1.0/framerate)
    
    errorY = yTarget - yPos-7.5
    integralY += float(errorY * dt)
    derivativeY = float(errorY - error_prevY)/(dt)
    
    yVel += (errorY * kP) + (integralY * kI) + (derivativeY * kD)

    errorX = xTarget - xPos-7.5
    integralX += (errorX * dt)
    derivativeX = (errorX - error_prevX)/(dt)
    
    xVel += (errorX * kP) + (integralX * kI) + (derivativeX * kD)
    
    xPos = xPos + xVel
    yPos = yPos + yVel

    error_prevY = errorY
    error_prevX = errorX

def setup():
    size(450, 255)
    background(204)
    stroke(0)
    frameRate(float(framerate)) #Slow it down a little
    global s
    s = Server(this, 12345)
def draw():
    background(204)
    global s
    if mousePressed == True:
        stroke(255)
        line(pmouseX, pmouseY, mouseX, mouseY)
        s.write(str(pmouseX) + " " + str(pmouseY) + " " + str(mouseX) + " " + str(mouseY) + "\n")
    c = s.available()
    if (c != None):
        input = c.readString()
        input_s = input.split('\n')
        data = map(int, input_s[0].encode('utf8').split(' '))
        stroke(0)
        # fill(255, 0, 0)
        # circle(float(data[2]), float(data[3]), 15)
        PID(float(data[2]),float(data[3]))
        fill(0, 255, 0)
        square(xPos, yPos, 15)
