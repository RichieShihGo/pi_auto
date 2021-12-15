import sys
import os
import requests
from time import sleep
import socket
import netifaces as ni

web_link_file = "/home/pi/pi_auto//udp/web_test.config"
config_folder  = "/home/pi/pi_auto/udp/server_config_dir"
hostname_file = "/etc/hostname"
file_list = os.listdir(config_folder)
    
def main():
    while True:
        try:
            ni.ifaddresses('wlan0')
            #print(len(ni.ifaddresses('wlan0')))
            #print("==========")
            if len(ni.ifaddresses('wlan0')) >= 3:
                client_ip=ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
                #print("===>")
                print("%s " % client_ip)
            
            #hostname
            hostname="raspberrypi"
            if os.path.exists(hostname_file):
        
                fp = open(hostname_file, "r")
                line=fp.readline()
                fp.close()

                line=line.replace("\n", "")

                hostname=line
                print("%s" % hostname)

            #web test
            web_ret=0
            if os.path.exists(web_link_file):

                fp = open(web_link_file, "r")
                line=fp.readline()
                fp.close()

                r=requests.get(line)

                print("%d" % r.status_code)
                if r.status_code == 200:
                    web_ret=1
            else:
                print("FileNotExist")

           
            for item in file_list:
                path = config_folder + '/' + item
        
                if os.path.exists(path):
                    with open (path , 'r') as r:
                        for line in r:
                            server_ip = line.split(' ')[0]
                            port = int(line.split(' ')[1])
                            print(server_ip,port)

                            #send udp
                            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
                                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                                s.sendto(send_data.encode('utf-8'), (server_ip, port))
                                s.close()
                else:
                   print("udp config not found")
            
        except Exception as e:
            print(e)
        sleep(60)

    
if __name__ == "__main__" :
    main()
        


