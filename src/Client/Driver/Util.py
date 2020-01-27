# Utility Functions


def sd(Cam, x, y, wd, ht):
    """Determines if an object is on the screen, return True. Used to optimize code by not drawing off-screen objects. Stands for 'should draw'"""
    if(x + wd >= -Cam.xshift and x  - wd <= -Cam.xshift + width and y + ht >= -Cam.yshift and y - ht <= -Cam.yshift + height):
        return True
    else:
        return False
    
def is_int(input):
    """Checks whether or not a value is an int. Used to check if data is corrupted during transfer between Server and Client"""
    try:
        num = int(input)
    except ValueError:
        return False
    return True
