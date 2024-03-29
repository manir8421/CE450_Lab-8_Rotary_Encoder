import RPi.GPIO as GPIO
import time

RoAPin = 11    # pin11 -> Connected to CLK
RoBPin = 12    # pin12 -> Connected to DT
RoSPin = 13    # pin13 -> Connected to SW
buzzerPin = 16 # pin16 -> Connected to the buzzer

globalCounter = 0

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

stepsPerRotation = 5  # Adjust circle according to counter

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RoAPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RoBPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RoSPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.output(buzzerPin, GPIO.HIGH)
    rotaryClear()

def beep():

    GPIO.output(buzzerPin, GPIO.LOW)
    time.sleep(1)  # Beep duration
    GPIO.output(buzzerPin, GPIO.HIGH)

def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)
    while(not GPIO.input(RoAPin)):
        Current_RoB_Status = GPIO.input(RoBPin)
        flag = 1
        time.sleep(0.002) 
    if flag == 1:
        flag = 0
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter -= 1
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter += 1

        print(f'globalCounter = {globalCounter}')

        if abs(globalCounter) >= stepsPerRotation:
            beep() 
            direction = 'Clockwise' if globalCounter > 0 else 'Counter-Clockwise'
            print(f'Beep! Full Rotation: {direction}')
            globalCounter = 0

def clear(ev=None):
    global globalCounter
    globalCounter = 0
    print('Reset: globalCounter = 0')
    time.sleep(1)

def rotaryClear():
    GPIO.add_event_detect(RoSPin, GPIO.FALLING, callback=clear)

def loop():
    while True:
        rotaryDeal()

def destroy():
    GPIO.cleanup()

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
