from SimpleCV import *
import time
from ledDb import *
from ledCalc import *

try:
    cam = Camera()
except:
    cam = Camera(1)
display = Display()

# suggestion Low limit calc
def sugLow(v, leftRange=30):
    if v-leftRange<0:
        return 0
    else:
        return v-leftRange
# suggestion Up limit cale
def sugUp(v, rightRange=30):
    if v+rightRange >255:
        return 255
    else:
        return v+rightRange

def getLow(input, pictureValue):
    if input == '' or input.upper() == 'Y':
        return sugLow(pictureValue)
    elif isinstance(eval(input), int):
        return eval(input)
    else:
        return 0

def getUp(input, pictureValue):
    if input == '' or input.upper() == 'Y':
        return sugUp(pictureValue)
    elif isinstance(eval(input), int):
        return eval(input)
    else:
        return 0

def drawOnLayer(layer):
    for row in led_table:
        mode = row[13]
        if (mode == 'CIRCLE' or mode == 'RING'):
            center = (row[2], row[3])
            r1 = row[4]
            r2 = row[5]
            if r1 > 0:
                layer.circle(center, r1)
            if r2 > 0:
                layer.circle(center,r2)
        elif mode == 'RECTANGLE':
            p1 = (row[2], row[3])
            size = (row[4],row[5])
            layer.rectangle(p1,size)

db = ledDb()
led_table = db.selectAllLed()
p1 = None
p2 = None
bb_list = []

while display.isNotDone():
    img = cam.getImage()
    layer = img.dl()
    drawOnLayer(layer)
    r = 6
    rr = 3

    dwn = display.leftButtonDownPosition()
    up = display.leftButtonUpPosition()

    R_dwn = display.rightButtonDownPosition()
    R_up = display.rightButtonUpPosition()

    if( dwn is not None and up is None):
        p1 = dwn
    if(p1 is not None and display.mouseLeft):
        w = display.mouseX - p1[0]
        l = display.mouseY - p1[1]
        hypotenuse = int(hypot(w,l))
        layer.rectangle(p1,(w,l), Color.GREEN)
        layer.circle(p1, hypotenuse, Color.GREEN)
        layer.circle(p1, hypotenuse+rr, Color.GREEN)
    if( dwn is None and  up is not None):
        p2 = up
        if p2 != p1:
            # bb = display.pointsToBoundingBox(p1, p2)
            # bb_list.append(bb)
            #--------------------------------------
            #if display.mouseLeft:
            xn = p1[0]
            yn = p1[1]
            new_circle = (xn, yn)
            print "Point:", new_circle


            save = raw_input("Save this point to local DB for test?(y/n)")
            if save == '' or save.upper() == 'Y' or save.upper() == 'YES':
                # --------------------------------------------------------------
                name = raw_input('Name of this:')
                print "name:", name

                mode = raw_input("mode [ 1:Circle(default), 2:Ring, 3:Rectangle]:?")
                if mode == '1' or mode == '' or mode.upper() == 'CIRCLE':
                    mode = 'CIRCLE'
                elif mode == '2' or mode.upper() == 'RING':
                    mode = 'RING'
                elif mode == '3' or mode.upper() == 'RECTANGLE':
                    mode = 'RECTANGLE'
                else:
                    mode = 'CIRCLE'
                print 'mode:', mode

                if mode == 'CIRCLE':
                    r1 = raw_input("r1 = %d ?" %hypotenuse)
                    if r1 == '':
                        r1 = hypotenuse
                    elif isinstance(eval(r1), int):
                        r1 = eval(r1)
                    else:
                        r1 = hypotenuse
                    print 'r1:', r1
                    r2 = 0
                    rgb1 = circleAvgRGB(img, new_circle, r1)
                    print "avgRGB in circle r=%d:" %r1, rgb1
                    rgb = rgb1
                elif mode == 'RING':
                    r1 = raw_input("r1 = %d ?" %hypotenuse)
                    if r1 == '':
                        r1 = hypotenuse
                    elif isinstance(eval(r1), int):
                        r1 = eval(r1)
                    else:
                        r1 = hypotenuse
                    print 'r1:', r1
                    r2 = raw_input("r2 = %d ?" %(hypotenuse+rr))
                    if r2 == '':
                        r2 = hypotenuse+rr
                    elif isinstance(eval(r2), int):
                        r2 = eval(r2)
                    else:
                        r2 = hypotenuse+rr
                    print 'r2:', r2
                    rgb2 = ringAvgRGB(img,new_circle, r1, r2)
                    print "avgRGB in ring(r1=%d, r2=%d):" %(r1,r2), rgb2
                    rgb =rgb2
                    # make sure r1>r2
                    if r1 < r2:
                        r1,r2 = r2,r1
                elif mode == 'RECTANGLE':
                    r1 = raw_input("Width = %d ?" %w)
                    if r1 == '':
                        r1 = w
                    elif isinstance(eval(r1), int):
                        r1 = eval(r1)
                    else:
                        r1 = w
                    print 'Width:', r1
                    r2 = raw_input("Length = %d ?" %l)
                    if r2 == '':
                        r2 = l
                    elif isinstance(eval(r2), int):
                        r2 = eval(r2)
                    else:
                        r2 = l
                    print 'Length:', r2
                    rgb3 = rectangleAvgRGB(img, new_circle, r1, r2)
                    print "avgRGB in rectangle =",rgb3
                    rgb = rgb3

                cs = raw_input("Color Space[1:RGB(default), 2:HSV, 3:HSL]:")
                if cs == '1' or cs == '' or cs.upper() == 'RGB':
                    cs = 'RGB'
                elif cs == '2' or cs.upper() == 'HSV':
                    cs = 'HSV'
                elif cs == '3':
                    cs == 'HSL' or cs.upper() == 'HSL'
                else:
                    cs = 'RGB'
                print 'Color Space:', cs

                if cs == 'RGB':
                    # ============ red =============
                    L1 = raw_input("Red low limit (picture value:%d) Use Suggest value=%d ?" %(rgb[0], sugLow(rgb[0])))
                    L1 = getLow(L1, rgb[0])
                    print 'Red low limit:', L1
                    U1 = raw_input("Red Up  limit(picture value:%d) Use Suggest Value=%d ?" %(rgb[0], sugUp(rgb[0])))
                    U1 = getUp(U1, rgb[0])
                    print 'Red Up  limit:', U1
                    # =========== blue =============
                    L2 = raw_input("Green low limit(picture value:%d) Use Suggest Value=%d ?" %(rgb[1], sugLow(rgb[1])))
                    L2 = getLow(L2, rgb[1])
                    print 'Green low limit:', L2
                    U2 = raw_input("Green Up  limit(picture value:%d) Use Suggest Value=%d ?" %(rgb[1], sugUp(rgb[1])))
                    U2 = getUp(U2, rgb[1])
                    print 'Green Up  limit:', U2
                    # =========== green ============
                    L3 = raw_input("Blue low limit(picture value:%d) Use Suggest Value=%d ?" %(rgb[2], sugLow(rgb[2])))
                    L3 = getLow(L3, rgb[2])
                    print 'Blue low limit:', L3
                    U3 = raw_input("Blue Up  limit(picture value:%d) Use Suggest Value=%d ?" %(rgb[2], sugUp(rgb[2])))
                    U3 = getUp(U3, rgb[2])
                    print 'Blue Up  limit:', U3

                    db.insertOneLedInfo(name=name,x=xn,y=yn,r1=r1,r2=r2,L1=L1,U1=U1,L2=L2,U2=U2,L3=L3,U3=U3,color_space=cs,mode=mode)
                    led_table = db.selectAllLed()
                    db.printAllLed()
                    # ------------------------
                else:
                    pass

    if (R_dwn is not None and R_up is None):
        R_p1 = R_dwn
    if (R_dwn is None and display.mouseRight):
        R_w = display.mouseX - R_p1[0]
        R_l = display.mouseY - R_p1[1]
        layer.rectangle(R_p1,(R_w,R_l),Color.RED)
    if (R_dwn is None and R_up is not None):
        R_p2 = R_up
        delete = raw_input("Delete in Rectangle[(%d,%d)--(%d,%d)] ?(y/n)" %(R_p1[0],R_p1[1],R_p2[0],R_p2[1]))
        if delete == '' or delete.upper() == 'Y' or delete.upper() == 'YES':
            row = db.selectOneLedNearIn2Points(R_p1[0],R_p1[1],R_p2[0],R_p2[1])
            if row is not None:
                print row
                id = row[0]
                rowCountDel = db.deleteOneLedById(id)
                print "%d row deleted!" %rowCountDel
                led_table = db.selectAllLed()
    img.save(display)
    # time.sleep(0.2)
db.close()
