# Utility Functions


def sd(Cam, x, y, wd, ht):
    """Determines if an object is on the screen, return True. Used to optimize code by not drawing off-screen objects. Stands for 'should draw'"""
    if(not Cam.spectatorMode):
        if(x + wd >= -Cam.xshift and x  - wd <= -Cam.xshift + width and y + ht >= -Cam.yshift and y - ht <= -Cam.yshift + height):
            return True
        else:
            return False
    else:
        return True
    
def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True
