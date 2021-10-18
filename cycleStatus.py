import os, subprocess
from datetime import date

def getOutputfromTerminal(command):
	proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	return output.decode('UTF-8')

os.system("echo '          "+date.today().strftime("%d-%b-%Y")+": ' >> cycleStatus.log")
os.system('system_profiler SPPowerDataType | grep "Cycle Count" >> cycleStatus.log')

if(getOutputfromTerminal('system_profiler SPPowerDataType | grep "Maximum Capacity"') == ''):
	os.system("echo '		  Replace Battery' >> cycleStatus.log")
else:
	os.system('system_profiler SPPowerDataType | grep "Maximum Capacity" >> cycleStatus.log')

os.system('echo "\n" >> cycleStatus.log')

with open('cycleStatus.log','r') as f:
	content = f.readlines()

cycleCount = [int(s) for s in content[-4].split() if s.isdigit()]

if('Replace' in content[-3]):
	maxCapacity = -1
	os.system("osascript -e 'display notification \"Capacity Exceeded: Replace Battery \" with title \"Cycle Count: "+str(cycleCount[0])+" \"  sound name \"Blow\"'")
else:
	maxCapacity = [int(s) for s in content[-3].replace("%","").split() if s.isdigit()]
	os.system("osascript -e 'display notification \"Max. Capacity: "+str(maxCapacity[0])+"% \" with title \"Cycle Count: "+str(cycleCount[0])+" \"  sound name \"Blow\"'")

#system_profiler SPPowerDataType | grep "Cycle Count"
#system_profiler SPPowerDataType | grep "State of Charge"
#system_profiler SPPowerDataType | grep "Maximum Capacity"

