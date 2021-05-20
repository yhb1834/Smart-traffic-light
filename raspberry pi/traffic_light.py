import RPi.GPIO as GPIO
import time
import os
import signal
import sys

# 차량 Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)     #Green
GPIO.setup(10, GPIO.OUT)    #left
GPIO.setup(11, GPIO.OUT)    #Yellow
GPIO.setup(12, GPIO.OUT)    #Red

# 보행자 Setup
GPIO.setup(13, GPIO.OUT)    #Green
GPIO.setup(14, GPIO.OUT)    #Red

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
	GPIO.output(9, False)
	GPIO.output(10, False)
	GPIO.output(11, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(14, False)    
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

#차량 탐지 signal
#  자회선 차선 차량
#  직진, 우회전 차량

#보행자 탐지 signal

#응급차량 탐지 signal

#사각지대 탐지 signal

#유동인구 고려 


# Loop forever
while True:
	# Red
	GPIO.output(12, True) 
	time.sleep(40)

    #보행자 신호
    GPIO.output(13, True)
    GPIO.output(14, False) 
    time.sleep(20)
    GPIO.output(13, False)
    GPIO.output(14, True)

	# Red and left
    GPIO.output(10, True)
    time.sleep(10)

	# Red and Yellow
	GPIO.output(11, True)
	time.sleep(5)

	# Green
    GPIO.output(9, False)
	GPIO.output(10, False)
	GPIO.output(11, False)
	GPIO.output(12, True)
	time.sleep(20)
	
    #Green and Yellow
	GPIO.output(9, False)
	GPIO.output(11, True)
	time.sleep(2)
	
	#Yellow off (red comes on at top of loop)
	GPIO.output(11, False)