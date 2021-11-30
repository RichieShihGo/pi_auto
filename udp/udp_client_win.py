import os
import socket
import requests
import platform
from time import sleep

web_link_file = r"C:\Users\jacky.lin\Desktop\web_test.config"
config_folder = r"C:\Users\jacky.lin\Desktop\Send_udp_new211129\server_config_dir"
file_list = os.listdir(config_folder)


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
    while True:
        try:
           #hostname
            platform.node()
            hostname=socket.gethostname()
            #client_ip 
            client_ip = get_ip()

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
                path = config_folder + '\\' + item
                
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


        

    





    






