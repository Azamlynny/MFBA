def sd(Cam, x, y, wd, ht): # Should Draw
    if(x + wd >= -Cam.xshift and x  - wd <= -Cam.xshift + width and y + ht >= -Cam.yshift and y - ht <= -Cam.yshift + height):
        return True
    else:
        return False
    
def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True