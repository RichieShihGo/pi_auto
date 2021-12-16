#-*- coding: utf-8 -*- 
#!/usr/bin/python  
import paramiko 
import threading 
def ssh2(ip,username,passwd,cmd): 
  try: 
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(ip,22,username,passwd,timeout=5) 
    for m in cmd: 
      stdin, stdout, stderr = ssh.exec_command(m) 
#      stdin.write("Y")  #簡單互動，輸入 ‘Y'
      for o in stdout:
            #out = stdout.readlines() 
            #螢幕輸出 
            #for o in out: 
        print (o) 
    print ('%s\tOK\n'%(ip))
    print('============')
    ssh.close() 
  except : 
    print ('%s\tError\n'%(ip))
    
if __name__=='__main__': 
  cmd = [
                 'cd /home/pi ; \
                 tar zxvf send_udp.tar.gz ; \
                 sudo chmod 644 pi_auto_new_setting.py ; \
                 sudo python3 pi_auto_new_setting.py ; \
                 cd /home/pi/pi_auto/clear ; \
                 chmod -R u=rw,go=r *  ; \
                 cd /home/pi/pi_auto/hostname_and_web ; \
                 chmod -R u=rw,go=r * ; \
                 cd /home/pi/pi_auto/reboot ;\
                 chmod -R u=rw,go=r * ; \
                 cd /home/pi/pi_auto/service ; \
                 chmod -R u=rw,go=r * ; \
                 cd /home/pi/pi_auto/udp ; \
                 chmod -R u=rw,go=r * ; \
                 chmod 755 server_config_dir ; \
                 cd /home/pi/pi_auto/udp/server_config_dir ; \
                 chmod -R u=rw,go=r * ; \
                 '
                ]
  
  username = "" #使;用者名稱 
  passwd = ""  #密碼 

  print ("Begin......")

ip = (
          '127.0.0.1',
          '127.0.0.2'
          )

for ip in ip:
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    a.start()




