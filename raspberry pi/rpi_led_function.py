#라즈베리 파이의 led의 전원을 켜고 끄는 간단한 기능을 구현해 놓은 코드입니다.
#프로토타입 코딩에서는 편의를 위하여 LED 번호를 프린팅하는 것으로 LED의 키고 끄는 것을 대신한 뒤, 라즈베리 파이에 구현 시 해당 기능을 사용할 예정입니다.

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

