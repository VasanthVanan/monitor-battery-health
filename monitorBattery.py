# -------------------------
#     Common Utilities
# -------------------------

import os
import datetime
import os.path, time
import requests
import subprocess
from datetime import date

class textcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getOutputfromTerminal(command):
	proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	return output.decode('UTF-8')

def readFile(fileName):
	with open(fileName,'r') as file:
		lines = file.readlines()
	return lines

# -----------------------------------
#     Battery Monitor Automation
# -----------------------------------

# ------ Variable Assignment by user --------

isMuted = True
apiToken = None
userToken = None
intervalValue = 2

# -------------------------------------------

charging = False
minuteFlag = False
maxCharge = 80
isExceeded = 350 # change according to time intervals

# read Previous Percentage for Comparison
previousPercentage = int(str(readFile('batteryPercentage.txt')).replace("\\n","")[2:-2])

# write current percentage over previous value
os.system('pmset -g batt | grep -Eo "\\d+%" | cut -d% -f1 > batteryPercentage.txt')

# read Current Percentage for Comparison
currentPercentage = int(str(readFile('batteryPercentage.txt')).replace("\\n","")[2:-2])

# Notification: Alert user to connect power source, if battery reaches 1% charge
if(currentPercentage == 1):
	os.system("osascript -e 'display notification \"Charge before it freaks you out \" with title \" ⚠️ 1% percentage left! \"  sound name \"Ping\"'")
	os.system('say "1 percent left. Charge before it freaks you out"')

# check the state of power source
if(currentPercentage > previousPercentage):
	charging = True

# read battery usage log file
content = readFile('tenMinjob.log') # replace tenMinjob.log if cron job runs for every 10 minutes

# calculate the difference of last record in log and current time 
gapTime = ((datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")) - (datetime.datetime.strptime(content[-1].strip()[:19],"%Y-%m-%d %H:%M:%S"))).seconds

# check if macbook is idle for 5 minutes
sleepSec = getOutputfromTerminal("echo $((`/usr/sbin/ioreg -c IOHIDSystem | sed -e '/HIDIdleTime/ !{ d' -e 't' -e '}' -e 's/.* = //g' -e 'q'` / 1000000000))") 

if(gapTime <= isExceeded):
	minuteFlag = True

if((str(maxCharge)+"% Crossed" not in content[-1])):

	if(((previousPercentage - currentPercentage) >= intervalValue) and not charging and minuteFlag):
		os.system("osascript -e 'display notification \"Monitor running applications \" with title \"Significant Energy is being used \"  sound name \"Blow\"'")
		if(not isMuted):
			os.system('say "Significant Energy is being used"')

	if(currentPercentage >= maxCharge):
		print(str(datetime.datetime.now())[:-7]+": - - - - "+str(maxCharge)+"% Crossed! - - - - ")
		if(int(sleepSec) >= 300):
			if(apiToken is not None and userToken is not None):
				requests.post(url="https://api.pushover.net/1/messages.json?token="+apiToken+"&user="+userToken+"&message=Macbook has reached "+str(currentPercentage)+"% Charge.&sound=classical&priority=1")
		else:
			os.system("osascript -e 'display notification \"Battery sufficiently charged \" with title \"Current Charge: "+str(currentPercentage)+"% \"  sound name \"Blow\"'")
			os.system('say "Macbook Air is sufficiently charged"')
	else:
		if(charging):
			print(str(str(datetime.datetime.now())[:-7])+": "+str(currentPercentage)+"% "+"(⚡️)")
		else:
			print(str(datetime.datetime.now())[:-7]+": "+str(currentPercentage)+"%")
else:
	if((int((datetime.datetime.now() - (datetime.datetime(int(content[-1][:19][:4]), int(content[-1][:19][5:7]), int(content[-1][:19][8:10]), int(content[-1][:19][11:13]), int(content[-1][:19][14:16]), int(content[-1][:19][17:19])))).total_seconds() / 60) > (60*2)) and (currentPercentage < maxCharge)):
		if(charging):
			print(str(str(datetime.datetime.now())[:-7])+": "+str(currentPercentage)+"%"+"(⚡️)")
		else:
			print(str(datetime.datetime.now())[:-7]+": "+str(currentPercentage)+"%")
