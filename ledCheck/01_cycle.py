from SimpleCV import *
import time

cam = Camera()
display = Display()

while display.isNotDone():
    img = cam.getImage()
    layer = img.dl()
    layer.circle((100, 100), 10)
    
    if display.mouseLeft:
        print str(display.mouseX), str(display.mouseY)
    elif display.mouseRight:
        break
    img.save(display)
    time.sleep(0.1)

