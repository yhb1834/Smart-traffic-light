import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(,GPIO.OUT)

while(True):
    GPIO.output(17,False)
    time.sleep(2)
    GPIO.output(17,True)
    time.sleep(2)
