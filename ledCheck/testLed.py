from SimpleCV import *
import time
from ledDb import *
from ledCalc import *

try:
    cam = Camera()
except:
    cam = Camera(1)
display = Display()

result = True
db = ledDb()
led_table = db.selectAllLed()
for i in range(0,30):
    img = cam.getImage()


for row in led_table:
    name = row[1]
    x = row[2]
    y = row[3]
    r1 = row[4]
    r2 = row[5]
    L1 = row[6]
    U1 = row[7]
    L2 = row[8]
    U2 = row[9]
    L3 = row[10]
    U3 = row[11]
    center = (x, y)
    color = circleAvgRGB(img, center, r1)
    r = color[0]
    g = color[1]
    b = color[2]
    res = r>=L1 and r<=U1 and g>=L2 and g<=U2 and b>=L3 and b<=U3
    print name, color, res
    result = result and res

print result
if result:
    print " _____         _____ _____ "
    print "|  __ \ /\    / ____/ ____|"
    print "| |__) /  \  | (___| (___  "
    print "|  ___/ /\ \  \___ \\__ _ \ "
    print "| |  / ____ \ ____) |___) |"
    print "|_| /_/    \_\_____/_____/ "
else:
    print " ______      _____ _      "
    print "|  ____/\   |_   _| |     "
    print "| |__ /  \    | | | |     "
    print "|  __/ /\ \   | | | |     "
    print "| | / ____ \ _| |_| |____ "
    print "|_|/_/    \_\_____|______|"
                           
img.save(display)
end = raw_input("input any key to exit")                           
                            
                            


