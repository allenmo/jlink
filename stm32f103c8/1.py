import os
import commands
import subprocess
'''
print '\n------os.system(cmd)--------------'
os.system('./1.sh')
print '\n------os.popen(cmd).read()--------------'
str = os.popen('./1.sh').read()
lines = str.split("\n")
for line in lines:
    print line

print '\n-----commands.getstatusoutput()--------------------------'
status, output = commands.getstatusoutput('./1.sh')
#status, output = commands.getstatusoutput('./JLinkExe -device STM32F103C8 -CommanderScript 1.jlink')
print status
print output
'''

#print '\n------subprocess.call(cmd, shell=True)-----------------------'
#subprocess.call('./1.sh', shell=True)

print '\n------subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True--------------------------'
subprocess.Popen('./1.sh', stdout=subprocess.PIPE, shell=True)
