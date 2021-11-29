import sys
import os
import requests
from time import sleep
import socket
import netifaces as ni

web_link_file="/home/pi/pi_auto/udp/web_test.config"

udp_server_file="/home/pi/pi_auto/udp/server_sigang.config"

udp_server2_file="/home/pi/pi_auto/udp/server_sinji.config"

hostname_file="/etc/hostname"

client_ip='0.0.0.0'
server_ip='10.193.5.102'
server2_ip='10.192.172.221'
port=60000
port2=60000


while(True):
    try:
        ni.ifaddresses('wlan0')
        #print(len(ni.ifaddresses('wlan0')))
        #print("==========")
        if len(ni.ifaddresses('wlan0')) >= 3:
            client_ip=ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
            #print("===>")
            print("%s " % client_ip)

            if os.path.exists(udp_server_file) and os.path.exists(udp_server2_file):
                        
                fp = open(udp_server_file, "r")
                line = fp.readline()
                fp.close()

                line=line.replace("\n", "")
                server_ip = line.split(" ")[0]
                port=int(line.split(" ")[1])

                fp2 = open(udp_server2_file,'r')
                line2 = fp2.readline()
                fp2.close()

                line2=line2.replace("\n","")
                server2_ip = line2.split(" ")[0]
                port2=int(line2.split(" ")[1])


                #print("%s" % server_ip)
                #print("%d" % port)

                #web test
                web_ret=0
                if os.path.exists(web_link_file):

                    fp = open(web_link_file, "r")
                    line=fp.readline()
                    fp.close()
                    
                    line=line.replace("\n","")
                    r=requests.get(line)

                    print("%d" % r.status_code)
                    if r.status_code == 200:
                        web_ret=1
                else:
                    print("FileNotExist")

                #hostname
                hostname="raspberrypi"
                if os.path.exists(hostname_file):
            
                    fp = open(hostname_file, "r")
                    line=fp.readline()
                    fp.close()

                    line=line.replace("\n", "")

                    hostname=line
                    print("%s" % hostname)

                else:
                    print("Hostname file not exist")

                #send udp to SiGang Server
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                s.sendto(send_data.encode('utf-8'), (server_ip, port))
                s.close()
                
                
                #send udp to SinJi Server
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                s.sendto(send_data.encode('utf-8'), (server2_ip, port2))
                s.close()
            else:
                print("udp config not found")
        else:
            print("wlan0 ip address is empty.")
    except Exception as e:
        print(e)


    sleep(60)
