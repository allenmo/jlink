from SimpleCV import *


disp = Display()
cam = Camera()

p1 = None
p2 = None
bb_list = []

while(disp.isNotDone()):
    img = cam.getImage()
    dwn = disp.leftButtonDownPosition()
    up = disp.leftButtonUpPosition()
    layer = img.dl()
    if( dwn is not None and up is None):
        p1 = dwn
    if( dwn is None and up is not None):
        p2 = up
        if p2 != p1: # filter out a kick
            bb = disp.pointsToBoundingBox(p1, p2)
            bb_list.append(bb)
    for b in bb_list:
        layer.rectangle((b[0],b[1]),(b[2],b[3]))
    #----------------------------
    if(p1 is not None and disp.mouseLeft): 
        w = disp.mouseX - p1[0]
        l = disp.mouseRawY - p1[1]
        layer.rectangle(p1,(w,l))
    img.save(disp)

