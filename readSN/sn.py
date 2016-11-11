import time
t0 = time.time()
from SimpleCV import *
import serial
import RPi.GPIO as GPIO

class camSnReader(object):
    def __init__(self, dev = 0):
        self.cam = Camera(dev, threaded=True)
        self.startButton = 7
        self.light = 11
        self.buzzerNo = 16
        self.buzzerInit()
        self.buzzer321()
        self.setSerial()
        self.lightInit()

    def readInLoop(self):
        ok = False
        n=0
        max_try = 50
        try:
            while(ok == False and n<max_try):
                img = self.cam.getImage()
                barcodes = img.findBarcode()
                if type(barcodes) == FeatureSet and len(barcodes) >=1:
                    ok = True
                    # img.save("1.jpg")
                    return barcodes[0].data, n
                else:
                    ok = False
                n = n +1
        except:
            print "in exception"
        return "",n
    
    def read(self, beep = True):
        sn = self.readInLoop()[0]
        if sn != "" and beep == True:
            self.buzzer1beep()
        return sn 
    
    def setSerial(
            self, 
            port = '/dev/serial0', 
            baudrate = 115200, 
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1):
        self.ser = serial.Serial(
            port = port, 
            baudrate = baudrate, 
            parity = parity,
            stopbits = stopbits,
            bytesize = bytesize,
            timeout = timeout)

    def readToSerial(self):
        GPIO.output(self.light, GPIO.LOW)
        sn = self.read(True)
        if sn != "":
            self.ser.write(sn + "\n")
        GPIO.output(self.light, GPIO.HIGH)

    def buzzerInit(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup([self.buzzerNo], GPIO.OUT, initial = GPIO.HIGH)

    def lightInit(self):
        GPIO.setup([self.light], GPIO.OUT, initial = GPIO.HIGH)

    def buzzer1beep(self):
        GPIO.output(self.buzzerNo, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.buzzerNo, GPIO.HIGH)

    def buzzer321(self):
        GPIO.output(self.buzzerNo, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.buzzerNo, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(self.buzzerNo, GPIO.LOW)
        time.sleep(0.15)
        GPIO.output(self.buzzerNo, GPIO.HIGH)
        time.sleep(0.05)

        GPIO.output(self.buzzerNo, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(self.buzzerNo, GPIO.HIGH)
        time.sleep(0.05)

    def enableBtn(self):
        GPIO.setup(self.startButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(self.startButton, GPIO.RISING, callback=self.btn_pressed_cb, bouncetime=5000)

    def btn_pressed_cb(self, channel):
        GPIO.remove_event_detect(self.startButton)
        self.readToSerial()
        print "debug 1"
        GPIO.add_event_detect(self.startButton, GPIO.RISING, callback=self.btn_pressed_cb, bouncetime=5000)
        print "debug 2"

if __name__ == "__main__":
    t1 = time.time()
    print t1-t0, "[firom SimpleCV import * time used]"
    reader = camSnReader()
    t2 = time.time()
    print t2-t1, "[cam = Camera() time used]"
    # print reader.read()
    # reader.readToSerial()
    t3 = time.time()
    print t3-t2, "[get image and findBarcode time used]"
    reader.enableBtn()
    while True:
        channel = GPIO.wait_for_edge(reader.startButton, GPIO.RISING, timeout=5000)
        if channel is None:
            print "no btn press"
        else:
            reader.readToSerial()
        #time.sleep(1)
    



