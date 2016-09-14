#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
import os
import commands
import re

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

readyLED = 11
inprocessLED = 13
passLED = 15
failLED = 37
startButton = 7
n=0
n_p=0
n_f=0

def mytime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def button_pressed_callback(channel):
    global n, n_p, n_f
    n += 1
    GPIO.remove_event_detect(startButton)
    print "channel:", channel
    print "Start Button pressed! GPIO CH:", channel
    print "Download FW Start[", mytime(), "]"
    GPIO.output(inprocessLED, GPIO.LOW)
    GPIO.output(passLED, GPIO.HIGH)
    GPIO.output(failLED, GPIO.HIGH)
   
    t1 = time.time() 
    #time.sleep(3)
    #subprocess.call('/home/pi/jlink/jlink/1.sh', shell=True)
    #subprocess.call('./JLinkExe -device STM32F103C8 -CommanderScript 1.jlink', shell=True)
    #subprocess.Popen('./1.sh', shell=True)
    #subprocess.Popen('./1.sh', stdout=subprocess.PIPE, shell=True)
    status, output = commands.getstatusoutput('./JLinkExe -device ATSAM4SD32C -JTAGConf -1,-1 -Speed 4000 -CommanderScript jtag.jlink')
    #status, output = commands.getstatusoutput('./1.sh')
    print "------------------------------------"
    print status, "\n"
    print output, "\n"

    GPIO.output(inprocessLED, GPIO.HIGH)
    match = re.search(pattern, output)
    if match:
        n_p += 1
        GPIO.output(passLED, GPIO.LOW)
        GPIO.output(failLED, GPIO.HIGH)
        print "Download pass"
    else:
        n_f += 1
        GPIO.output(passLED, GPIO.HIGH)
        GPIO.output(failLED, GPIO.LOW)
        print "Download fail"

    t2 = time.time()
    print "Download FW end[", mytime(), "]"
    print "Time used:", (t2-t1)
    print "Total Programed:", n, "\tPass:", n_p, "\tFail:", n_f
    print "===================================="
    print "\n"
    print "Waiting for start button press..."
    GPIO.add_event_detect(startButton, GPIO.RISING, callback=button_pressed_callback, bouncetime=400)

print "Program start[", mytime(), "]"

GPIO.setup([readyLED, inprocessLED, passLED, failLED], GPIO.OUT, initial=GPIO.HIGH)
time.sleep(0.3)
GPIO.output(readyLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(inprocessLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(passLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(failLED, GPIO.LOW)
time.sleep(0.3)
GPIO.output(failLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(passLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(inprocessLED, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(readyLED, GPIO.HIGH)
time.sleep(0.3)
for i in range(0,6):
    GPIO.output(readyLED, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(readyLED, GPIO.HIGH)
    time.sleep(0.1)
GPIO.output(readyLED, GPIO.LOW)
pattern = re.compile('Verifying flash(.*?)100%(.*?)Done', re.S)

GPIO.setup(startButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(startButton, GPIO.RISING, callback=button_pressed_callback, bouncetime=400)
print "Waiting for start button press..."

while True:
    #print "in loop"
    time.sleep(0.5)
