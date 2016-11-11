from SimpleCV import *
import time

cam = Camera()
display = Display()
circle_list = [(207, 261), (207, 362)]

def circleAvgRGB(img, center, r=8):
    in_range_points = []
    x = center[0]
    y = center[1]
    print "x, y:", x, y
    x0 = x-r
    y0 = y-r
    xn = x+r
    yn = y+r
    print "x0, y0, xn, yn:", x0, y0, xn, yn
    for j in range(x0, xn):
        for k in range(y0, yn):
            rjk = hypot(j-x, k-y)
            if rjk < r:
                in_range_point = (j, k, rjk)
                in_range_points.append(in_range_point)


    return in_range_points



while display.isNotDone():
    img = cam.getImage()
    layer = img.dl()
    for circle in circle_list:
        layer.circle(circle, 8)

    if display.mouseLeft:
        new_circle = (display.mouseX, display.mouseY)
        print new_circle
        circle_list.append(new_circle)
        print "r, g, b:", img[display.mouseX, display.mouseY]
        list = circleAvgRGB(img, new_circle, r=8)
        print "len of in range points:", len(list)
        # print list

        # imgHSV = img.toHSV()
        # print "h, s, v:", imgHSV.getPixel(display.mouseX, display.mouseY)


    elif display.mouseRight:
        break                                                            
    img.save(display)
    time.sleep(0.1)

