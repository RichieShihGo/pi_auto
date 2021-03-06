import sys
import os
#path of hostname and web rul
hostname_web_config_file_path = "/home/pi/pi_auto/hostname_and_web/hostname_web.config"
#path of web_test 
web_test_file_path = "/home/pi/pi_auto/udp/web_test.config"
#path of autostart (need icewease)
autostart_file_path = "/home/pi/.config/lxsession/LXDE-pi/autostart"
#path of hostname
hostname_file_path = "/etc/hostname"
#path of hosts , It need to change device name and set NTP server .
hosts_file_path = "/etc/hosts"
#path of ntp.conf , It need to add one command in last line.
ntpconf_file_path="/etc/ntp.conf"

hostname = "raspberrypi"
weblink = "http://192.1.1.59/aqc/aqc009.aspx?tc_qc0704=TQ"

     
def setAutoStart(): #write autostart
    with open(autostart_file_path, "w")as fp:
        fp.write("@xset s off\n")
        fp.write("@xset s noblank\n")
        fp.write("@xset -dpms\n\n")
        firefox_web_string = '@sudo -u pi iceweasel %s\n\n' % weblink 
        fp.write(firefox_web_string)
        fp.write("@lxpanel --profile LXDE-pi\n")
        fp.write("@pcmanfm --desktop --profile LXDE-pi\n")
        fp.write("@/home/pi/start_delay.sh\n")
    print("Setted autostart.")

def setHostName():  #write hostname
    with open(hostname_file_path, "w")as fp:
        fp.write(hostname)
    print("Setted HostName : "+hostname)

def setWebTest():        #write web_test.config
    with open(web_test_file_path, "w")as fp:
        fp.write(weblink)
    print("Setted Weblink: "+weblink)

def setHosts():#Write Hosts
    with open(hosts_file_path,'w')as fp:
        fp.write("127.0.0.1\tlocalhost\n")
        fp.write("::1\t\tlocalhost ip6-localhost ip6-loopback\n")
        fp.write("ff02::1\t\tip6-allnodes\n")
        fp.write("ff02::2\t\tip6-allrouters\n\n")
        fp.write("127.0.1.1\t"+hostname+"\n")
        fp.write("10.192.5.3\tNTP-server-host\n")
    print("Setted Hosts.")

def setNtpConf(): #Write ntp.conf 
    with open(ntpconf_file_path,'a')as fp:
        fp.write("\nserver NTP-server-host prefer iburst")
    print("ntp.config Setted ")

if os.path.exists(hostname_web_config_file_path):
    fp = open(hostname_web_config_file_path, "r")
    line = fp.readline()
    line = line.replace("\n", "")
    fp.close()

    try:
        hostname = line.split(" ")[0]
        weblink = line.split(" ")[1]

        print("hostname = %s, weblink = %s" % (hostname, weblink))

        #write hostname
        setHostName()
        #write web_test.config
        setWebTest() 
        #write autostart
        setAutoStart()
        #Write Hosts
        setHosts()
        #Write ntp.conf 
        setNtpConf()

        hostname = line.split
    except Exception as e:
        print(e)

    

else:
    print("There is no hostname_web.config.")

