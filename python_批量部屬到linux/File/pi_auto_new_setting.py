import os
import sys 

#setting log path
log_path = "/home/pi/configChange.log"

#check pi_auto or pi4_auto paht of "hostnamt_and_web.config" 
pi4_auto_hn_path = "/home/pi/pi4_auto/hostname_and_web/hostname_web.config"
pi_auto_hn_path = "/home/pi/pi_auto/hostname_and_web/hostname_web.config"

#check pi_auto or pi4_auto paht of "web_test.config" 
pi4_auto_wt_path = "/home/pi/pi4_auto/udp/web_test.config"
pi4_auto_wt_path1 = "/home/pi/pi4_auto/web_test.config"
pi_auto_wt_path = "/home/pi/pi_auto/udp/web_test.config"

#set service path
py_service_path = "/home/pi/pi_auto/service/"
service_path = "/etc/systemd/system/"

def checkFile():
    if os.path.exists(pi4_auto_hn_path):
        os.system('sudo mv '+pi4_auto_hn_path+' '+pi_auto_hn_path)
        with open(log_path,'a') as fw:
            fw.write('The hostname_and_web.config of pi4_auto be move to pi_auto.\n') 
    else:
        with open(log_path,'a') as fw:
            fw.write('not found the config of pi4_auto.\n')
    if os.path.exists(pi4_auto_wt_path):
        os.system('sudo mv '+pi4_auto_wt_path+' '+pi_auto_wt_path)
        with open(log_path,'a') as fw:
            fw.write('The web_test.config of pi4_auto be move to pi_auto.\n')
    else:
        if os.path.exists(pi4_auto_wt_path1):
            os.system('sudo mv '+pi4_auto_wt_path1+' '+pi_auto_wt_path)
            with open(log_path,'a') as fw:
                fw.write('The web_test.config of pi4_auto be move to pi_auto.\n')
        else:
            with open(log_path,'a') as fw:
                fw.write('not found the config of pi4_auto.\n')

def finalCheck():
    if os.path.exists(pi_auto_hn_path):
        with open(log_path,'a') as fw:
            fw.write('HostName_web.config 存在\n')
    else:
        with open(log_path,'a') as fw:
            fw.write('HostName_web.config  不存在\n')
    if os.path.exists(pi_auto_wt_path):
        with open(log_path,'a') as fw:
            fw.write('Web_test.config 存在\n')
    else:
        with open(log_path,'a') as fw:
            fw.write('Web_test.config 不存在\n')

def serviceUpdate():
    os.system('sudo cp '+py_service_path+'* '+service_path )
    os.system('sudo systemctl daemon-reload')
    os.system('sudo systemctl restart  clear_cache.service')
    os.system('sudo systemctl restart  reboot_button.service')
    os.system('sudo systemctl restart  reboot_timer.service')
    os.system('sudo systemctl restart  udp_client.service')
    with open(log_path,'a') as fw:
        fw.write('Service was be updated\n')
try:
    #check hostname url config path ,web test path and change it
    checkFile()
    #check hostname url config ,web test.
    finalCheck()
    #update service
    serviceUpdate()
except Exception as e:
    print(e)
