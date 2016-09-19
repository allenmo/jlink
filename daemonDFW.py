#!/usr/bin/env python
import subprocess
import commands
import time
import re

while True:
    status, output = commands.getstatusoutput('ps aux |grep downloadFW')
    pattern = re.compile('downloadFW_JTAG', re.S)
    match = re.search(pattern, output)
    if match:
        print "program is running, no need to start"
    else:
        print "program not run yet, now will start"
        subprocess.Popen(r'python downloadFW_JTAG.py', shell=True)
        time.sleep(5)
    print status 
    print output
    time.sleep(5)
