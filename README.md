            
 San Francisco Bay University

CE450 Fundamentals of Embedded Engineering
Lab 8 Rotary Encoder Design

Objectives:
The rotary encoder is popularly used in the control system. In this week, students will design the program to control rotary encoder through GPIO ports on Raspberry Pi bord and do hands-on exercise through lab assignments.

Introduction:
A rotary encoder is an electro-mechanical device that converts the angular position or motion of a shaft or axle to analog or digital code. Rotary encoders are usually placed at the side which is perpendicular to the shaft. They act as sensors for detecting angle, speed, length, position, and acceleration in automation field.

Equipment: 
The equipment you require is as follows:
•	Laptop & Raspberry Pi 3 model Board
•	SunFounder Super Starter Kit V2.0 for Raspberry Pi 
•	One Rotary Encoder module

The Laboratory Procedure: 
1.	Hardware connection 

 
 
 

2.	Control program in Python

# Python Program

import RPi.GPIO as GPIO
import time

RoAPin = 11    # pin11	-> Connected to CLK
RoBPin = 12    # pin12	-> Connected to DT
RoSPin = 13    # pin13	-> Connected to SW

globalCounter = 0

flag = 0
Last_RoB_Status = 0		# two var. for pin B’s value	
Current_RoB_Status = 0		

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RoAPin, GPIO.IN)    # input mode
	GPIO.setup(RoBPin, GPIO.IN)
	GPIO.setup(RoSPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Bottom pin
	rotaryClear()

def rotaryDeal():
	global flag
	global Last_RoB_Status
	global Current_RoB_Status
	global globalCounter
	Last_RoB_Status = GPIO.input(RoBPin)	# Read in data from DT
	while(not GPIO.input(RoAPin)):
		Current_RoB_Status = GPIO.input(RoBPin)
		flag = 1
	if flag == 1:
		flag = 0
		if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
			globalCounter = globalCounter + 1
			print 'globalCounter = %d' % globalCounter
		if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
			globalCounter = globalCounter - 1
			print 'globalCounter = %d' % globalCounter

def clear(ev=None):
        	globalCounter = 0
	print 'globalCounter = %d' % globalCounter
	time.sleep(1)

def rotaryClear():
        GPIO.add_event_detect(RoSPin, GPIO.FALLING, callback=clear) 	
	# wait for falling

def loop():
	global globalCounter
	while True:
		rotaryDeal()
#		print 'globalCounter = %d' % globalCounter

def destroy():
	GPIO.cleanup()             # Release resource
setup()
try:
	loop()
except 	KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()

	*Note: Hardware connection reference and running command
https://learn.sunfounder.com/lesson-12-rotary-encoder/
https://learn.sunfounder.com/category/super-kit-v3-0-for-raspberry-pi/

The Laboratory Assignments: 

1.	Build up the hardware circuit and run the example program to observe what will happen.

2.	Add a buzzer to the above circuit and design the program to make “z” sound as the turning indicator if the encoder is turned one circle. 
