import os
import requests
from time import sleep
import socket
#import netifaces as ni
import platform


config = r"C:\Users\jacky.lin\Desktop\server_config_dir" #Server config檔目錄




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


def validIPv4Address(ipaddr):
    ret = False

    try:
        socket.inet_aton(ipaddr)
        ret = True
        print("valid ipv4 address")
    except socket.error:
        print("socket error")
    
    return ret

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    web_ret = 0
    while True:
        try:
            client_ip = get_ip()
            r=requests.get(web_link_file)
            print("%d" % r.status_code)
            if r.status_code == 200:
                web_ret=1
                
            #hostname
            platform.node()
            hostname=socket.gethostname()

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









