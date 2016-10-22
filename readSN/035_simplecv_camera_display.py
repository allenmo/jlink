from SimpleCV import Camera, Display, Image

cam = Camera()
display = Display()

while(display.isNotDone()):
    img = cam.getImage()
    img.save( display )

