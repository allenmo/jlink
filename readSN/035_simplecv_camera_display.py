import time
from SimpleCV import Camera, Display, Image

cam = Camera()
display = Display()

while(display.isNotDone()):
    t0 = time.time()
    img = cam.getImage()
    img.save( display )
    t1 = time.time()
    print t1-t0

