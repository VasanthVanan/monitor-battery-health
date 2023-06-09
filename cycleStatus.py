import os, subprocess, re
from datetime import date

def getOutputfromTerminal(command):
	proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	return output.decode('UTF-8')

os.system("echo '          "+date.today().strftime("%d-%b-%Y")+": ' >> ~/monitor-battery-health/cycleStatus.log")
os.system('system_profiler SPPowerDataType | grep "Cycle Count" >> ~/monitor-battery-health/cycleStatus.log')

if(getOutputfromTerminal('system_profiler SPPowerDataType | grep "Maximum Capacity"') == ''):
	os.system("echo '		  Maximum Capacity: 0' >> ~/monitor-battery-health/cycleStatus.log")
else:
	os.system('system_profiler SPPowerDataType | grep "Maximum Capacity" >> ~/monitor-battery-health/cycleStatus.log')

os.system('echo "\n" >> ~/monitor-battery-health/cycleStatus.log')

with open('cycleStatus.log','r') as f:
	content = f.readlines()

cycleCount = [int(s) for s in content[-4].split() if s.isdigit()]

if('Replace' in content[-3] and int(re.findall(r'\d+',content[-4])[0]) >= 1000):
	maxCapacity = -1
	os.system("osascript -e 'display notification \"Capacity Exceeded: Replace Battery \" with title \"Cycle Count: "+str(cycleCount[0])+" \"  sound name \"Blow\"'")
else:
	maxCapacity = [int(s) for s in content[-3].replace("%","").split() if s.isdigit()]
	if maxCapacity[0] == 0:
		os.system("osascript -e 'display notification with title \"Cycle Count: "+str(cycleCount[0])+" \"  sound name \"Blow\"'")
		
	else:
		os.system("osascript -e 'display notification \"Max. Capacity: "+str(maxCapacity[0])+"% \" with title \"Cycle Count: "+str(cycleCount[0])+" \"  sound name \"Blow\"'")

#system_profiler SPPowerDataType | grep "Cycle Count"
#system_profiler SPPowerDataType | grep "State of Charge"
#system_profiler SPPowerDataType | grep "Maximum Capacity"
