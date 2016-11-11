from SimpleCV import *

def circleAvgRGB(img, center, r=8):
    points = inCirclePoints(center, r)
    n = len(points)
    sumR = 0
    sumG = 0
    sumB = 0
    for point in points:
        sumR = sumR + img[point[0], point[1]][0]
        sumG = sumG + img[point[0], point[1]][1]
        sumB = sumB + img[point[0], point[1]][2]
    avgR = int(sumR/n)
    avgG = int(sumG/n)
    avgB = int(sumB/n)
    # print sumR, sumG, sumB
    # print avgR, avgG, avgB
    return avgR, avgG, avgB

def ringAvgRGB(img, center, r1=8, r2=6):
    points = inRingPoints(center, r1, r2)
    n = len(points)
    sumR = 0
    sumG = 0
    sumB = 0
    for point in points:
        sumR = sumR + img[point[0], point[1]][0]
        sumG = sumG + img[point[0], point[1]][1]
        sumB = sumB + img[point[0], point[1]][2]
    avgR = int(sumR/n)
    avgG = int(sumG/n)
    avgB = int(sumB/n)
    # print sumR, sumG, sumB
    # print avgR, avgG, avgB
    return avgR, avgG, avgB

def rectangleAvgRGB(img,p1, w, l):
    points = inRectanglePoints(p1,w,l)
    n = len(points)
    sumR = 0
    sumG = 0
    sumB = 0
    for point in points:
        sumR = sumR + img[point[0], point[1]][0]
        sumG = sumG + img[point[0], point[1]][1]
        sumB = sumB + img[point[0], point[1]][2]
    avgR = int(sumR/n)
    avgG = int(sumG/n)
    avgB = int(sumB/n)
    # print sumR, sumG, sumB
    # print avgR, avgG, avgB
    return avgR, avgG, avgB

def inCirclePoints(center, r=8):
    in_range_points = []
    x = center[0]
    y = center[1]
    # print "x, y:", x, y
    x0 = x-r
    y0 = y-r
    xn = x+r
    yn = y+r
    # print "x0, y0, xn, yn:", x0, y0, xn, yn
    for j in range(x0, xn+1):
        for k in range(y0, yn+1):
            rjk = hypot(j-x, k-y)
            if rjk <= r:
                in_range_point = (j, k)
                in_range_points.append(in_range_point)
    return in_range_points

def inRingPoints(center, r1=8, r2=6):
    in_range_points = []
    R = max(r1, r2)
    r = min(r1, r2)
    x = center[0]
    y = center[1]
    x0 = x - R
    y0 = y - R
    xn = x + R
    yn = y + R
    for j in range(x0, xn+1):
        for k in range(y0, yn+1):
            rjk = hypot(j-x, k-y)
            if rjk <= R and rjk > r:
                in_range_point = (j,k)
                in_range_points.append(in_range_point)
    return in_range_points

def inRectanglePoints(p1, w=8, l=6):
    in_range_points = []
    x = p1[0]
    y = p1[1]
    for j in range(x,x+w):
        for k in range(y,y+l):
            in_range_point = (j,k)
            in_range_points.append(in_range_point)
    return in_range_points

