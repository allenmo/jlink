#!/usr/bin/env python
import subprocess
import commands
import time
import re

while True:
    time.sleep(2)
    status, output = commands.getstatusoutput('ps aux |grep downloadFW')
    pattern = re.compile('downloadFW_JTAG', re.S)
    match = re.search(pattern, output)
    if match:
        print "program is running, no need to start"
    else:
        print "program not run yet, now will start"
        #a,b = commands.getstatusoutput('cd /home/pi/jlink/jlink')
        #status2, output2 = commands.getstatusoutput(r'python downloadFW_JTAG.py \&')
        #status2, output2 = commands.getstatusoutput(r'./downloadFW_JTAG.py \&')
        #---->subprocess.call(r'python downloadFW_JTAG.py', shell=True)
        subprocess.Popen(r'python downloadFW_JTAG.py', shell=True)

        #print status2
        #print output2
        time.sleep(5)
    print status 
    print output
