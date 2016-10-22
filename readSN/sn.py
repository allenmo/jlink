import time
t0 = time.time()
from SimpleCV import *

def readFromCamera(cam):
    ok = False
    n=0
    max_try = 50
    while(ok == False and n<max_try):
        img = cam.getImage()
        barcodes = img.findBarcode()
        if type(barcodes) == FeatureSet and len(barcodes) >=1:
            ok = True
            # img.save("1.jpg")
            return barcodes[0].data, n
        else:
            ok = False
        n = n +1
    return "",n

if __name__ == "__main__":
    t1 = time.time()
    print t1-t0, "[firom SimpleCV import * time used]"
    cam = Camera()
    t2 = time.time()
    print t2-t1, "[cam = Camera() time used]"
    print readFromCamera(cam)
    t3 = time.time()
    print t3-t2, "[get image and findBarcode time used]"



