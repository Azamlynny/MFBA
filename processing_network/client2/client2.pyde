add_library('net')
c2 = Client
input = ""
data = []

def setup():
    size(450, 255); 
    background(204);
    stroke(0);
    frameRate(30) #Slow it down a little
    #Connect to the server’s IP address and port­
    global c2
    c2 = Client(this, "127.0.0.1", 12345); #Replace with your server’s IP and port
    
def draw():
    global c2
    stroke(255)
    line(pmouseX, pmouseY, mouseX, mouseY)
    c2.write(str(pmouseX) + " " + str(pmouseY) + " " + str(mouseX) + " " + str(mouseY) + "\n")

    if c2.available() > 0:
        input = c2.readString()
        input_s = input.split("\n")
        data = int(input_s[0].encode('utf8').split(' '))
        stroke(0);
        line(data[0], data[1], data[2], data[3])
