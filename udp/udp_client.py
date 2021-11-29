import os
import requests
from time import sleep
import socket
import netifaces as ni



config = r"/home/pi/pi_auto/udp/server_config_dir" #Server config檔目錄


hostname_file="/etc/hostname"

file = os.listdir(config) #取得目錄下的所有文件
server_config_list = [ ]


for file in file: #遍歷目錄
    if not os.path.isdir(file): #判斷不是文件夾才打開
        with open (config+'/'+file) as f: #用with open 打開文件
            iter_f = iter(f) #創造疊代器
            str = " "
            for line in iter_f:  #遍歷文件，逐行遍歷，讀取文件
                str = str + line
            server_config_list .append(str) #將每個目錄的文件存到list中
            server_config_list.sort()
        
            


server_new = server_config_list[0]
server_new_ip = server_new.split()[0]
server_new_port =  int(server_new.split()[1])

server_sigang = server_config_list[1]
server_sigang_ip = server_sigang.split()[0]
server_sigang_port = int(server_sigang.split()[1])

server_sinji = server_config_list[2]
server_sinji_ip = server_sinji.split()[0]
server_sinji_port = int(server_sinji.split()[1])

web_link_file = server_config_list[3]


def main():
    web_ret = 0
    while True:
        try:
            ni.ifaddresses('wlan0')
            if len(ni.ifaddresses('wlan0')) >= 3:
                client_ip=ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
                #print("===>")
                print("%s " % client_ip)
                
            #web test
            web_ret=0
            r=requests.get(web_link_file)
            print("%d" % r.status_code)
            if r.status_code == 200:
                web_ret=1

            #hostname
            if os.path.exists(hostname_file):
                 with open (hostname_file,'r') as r:
                     line = r.readline()
                     line = line.replace("\n","")
                     hostname = line
                     print("%s"%hostname)

            #send udp server_new 
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                s.sendto(send_data.encode('utf-8'), (server_new_ip, server_new_port))
                s.close()
            #send udp server_sigang
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                s.sendto(send_data.encode('utf-8'), (server_sigang_ip, server_sigang_port))
                s.close()
            #send udp server_sinji
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
                send_data = '%s %s %d' % (hostname,client_ip,web_ret)
                s.sendto(send_data.encode('utf-8'), (server_sinji_ip, server_sinji_port))
                s.close()

        except Exception as e:
            print(e)

        sleep(60)


if __name__ == "__main__" :
    main()









