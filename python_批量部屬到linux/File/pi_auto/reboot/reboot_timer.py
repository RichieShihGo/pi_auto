import sys
import time
from time import sleep
import os
from datetime import datetime
import subprocess

reboot_time_file = "/home/pi/pi_auto/reboot/reboot_timer.config"

prevent = True

def runReboot():
    command = ['reboot']

    ret = str(subprocess.check_output(command, shell=True))

    return ret

while True:

    reboot_time = "03:00" #default
    if os.path.exists(reboot_time_file): #if config is set, will replace with new time
        fp = open(reboot_time_file, "r")
        #clear_time = "15:00"
        reboot_time = fp.readline()
        reboot_time = reboot_time.replace("\n", "")
        fp.close()
        
    #print("==> %s" % reboot_time)
    

    current_time = datetime.today().strftime("%2H:%2M")
     
    if current_time == reboot_time and prevent == False:

        print("reboot!")
        ret = runReboot()

    prevent = False

    sleep(60)
