#-*- coding: utf-8 -*- 
#!/usr/bin/python  
import paramiko 
import threading


def sftp(ip,username,passwd,remotepath):
    try:
        #獲取Transport例項 
        tran = paramiko.Transport(ip,port) 
        #連線SSH服務端 
        tran.connect(username = username, password = passwd)
        #獲取SFTP例項 
        sftp = paramiko.SFTPClient.from_transport(tran) 
        #設定上傳的本地/遠端檔案路徑 
        localpath=r'C:\Users\jacky.lin\Desktop\python_批量部屬到linux\send_udp.tar.gz' ##本地檔案路徑
        #localpath=r'C:\Users\jacky.lin\Desktop\wifi.py'
     
        #執行上傳動作 
        sftp.put(localpath,remotepath)
        print('File Successfully transmitted...')
        print ('%s\tOK\n'%(ip))
        print('============')
        tran.close()
    except : 
        print ('%s\tError\n'%(ip))

if __name__=='__main__':
    port = 22
    username = 'pi'
    passwd = 'Magton!c'
    remotepath="/home/pi/send_udp.tar.gz" ##上傳物件儲存的檔案路徑
    #remotepath="/home/pi/pi_auto/udp/123.py"
    threads = []  #多執行緒


ip = ('10.192.172.120','10.192.172.116')

for ip in ip:
    a=threading.Thread(target=sftp,args=(ip,username,passwd,remotepath))
    a.start()








##if __name__=='__main__':
##  username = "pi" #使用者名稱
##  port = 22
##  passwd = "Magton!c"  #密碼 
##  threads = []  #多執行緒 
##  print ("Begin......")
##  
##ip = ('10.192.172.120','10.192.172.116')
##
##for ip in ip:
##    a=threading.Thread(target=sftp,args=(ip,port,username,passwd))
##    a.start()

