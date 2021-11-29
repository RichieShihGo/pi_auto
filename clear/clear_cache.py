import sys
import time
from time import sleep
import os
from datetime import datetime
import subprocess


clear_cache_file="/home/pi/pi_auto/clear/clear_cache.config"

def clearCache():
    command = ['echo 3 > /proc/sys/vm/drop_caches']

    ret = str(subprocess.check_output(command, shell=True))

    return ret

def runWiFiPowerSaveOff():
    command = ['/sbin/iw dev wlan0 set power_save off']

    ret = str(subprocess.check_output(command, shell=True))
    
    return ret

clearMin=60
minCount=0

wifiPowerSaveOff=False

while True:

    if not wifiPowerSaveOff:
        ret = runWiFiPowerSaveOff()
        wifiPowerSaveOff=True
    
    clear_time="08:00" #default
    if os.path.exists(clear_cache_file): #if config is set, will replace with new time
        fp = open(clear_cache_file, "r")
        #clear_time = "15:00"
        clear_time = fp.readline()
        clear_time = clear_time.replace("\n", "")
        fp.close()
        
    #print("==> %s" % clear_time)

    current_time = datetime.today().strftime("%2H:%2M")
    
    if current_time == clear_time:
        print("time match!")
        #ret = clearCache()

    if minCount > clearMin:
        ret = clearCache()
        minCount = 0
    
    minCount = minCount + 1

    sleep(60)
