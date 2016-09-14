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

def button_pressed_callback(channel):
    GPIO.remove_event_detect(startButton)
    print "channel:", channel
    print "Start Button pressed!"
    GPIO.output(inprocessLED, GPIO.LOW)
    GPIO.output(passLED, GPIO.HIGH)
    GPIO.output(failLED, GPIO.HIGH)
   
    t1 = time.time() 
    #time.sleep(3)
    #subprocess.call('/home/pi/jlink/jlink/1.sh', shell=True)
    #subprocess.call('./JLinkExe -device STM32F103C8 -CommanderScript 1.jlink', shell=True)
    #subprocess.Popen('./1.sh', shell=True)
    #subprocess.Popen('./1.sh', stdout=subprocess.PIPE, shell=True)
    status, output = commands.getstatusoutput('./JLinkExe -device STM32F103C8 -CommanderScript 1.jlink')
    #status, output = commands.getstatusoutput('./1.sh')
    t2 = time.time()
    print "------------------------------------"
    print status, "\n"
    print output, "\n"
    print "Time used:", (t2-t1)
    print "===================================="
    print "Waiting for start button press..."

    GPIO.output(inprocessLED, GPIO.HIGH)
    match = re.search(pattern, output)
    if match:
        GPIO.output(passLED, GPIO.LOW)
        GPIO.output(failLED, GPIO.HIGH)
    else:
        GPIO.output(passLED, GPIO.HIGH)
        GPIO.output(failLED, GPIO.LOW)
    GPIO.add_event_detect(startButton, GPIO.RISING, callback=button_pressed_callback, bouncetime=400)

GPIO.setup(startButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(startButton, GPIO.RISING, callback=button_pressed_callback, bouncetime=400)
print "Waiting for start button press..."

while True:
    #print "in loop"
    time.sleep(0.5)
