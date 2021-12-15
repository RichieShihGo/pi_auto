from gpiozero import Button 
from signal import pause
import subprocess

def reboot():
    print("reboot")
    subprocess.call(['shutdown', '-r', 'now'], shell=False)

button = Button(21, hold_time=3)
button.when_held = reboot
#button.when_pressed  = reboot

pause()
