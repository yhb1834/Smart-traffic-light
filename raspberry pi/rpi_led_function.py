import RPI.GPIO as GPIO
from time import sleep

green=17

#set gpio in bcm mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(green,GPIO.OUT)

while(True):
    GPIO.output(green,False)
    time.sleep(2)
    GPIO.output(green,True)
    time.sleep(2)
