from machine import Pin,PWM
from pwm import myPWM
import time

mypwm = myPWM(15,2,0,4,5,18,19,21)
chns=[0,1,2,3,4,5,6,7]
dutys=[0,0,0,0,0,0,0,0,1023,512,256,128,64,32,16,8,0,0,0,0,0,0,0,0]
delayTimes=50

# buttons changing direction of floating light
buttonRightToLeft = Pin(13, Pin.IN,Pin.PULL_UP) 
buttonLeftToRight = Pin(14, Pin.IN,Pin.PULL_UP) 

def lightUp(order):
        if(order ==1):
            while True:
                for i in range(0,16):
                    if not buttonLeftToRight.value(): 
                        # direction change
                        lightUp(0)
                    for j in range(0,8):
                        mypwm.ledcWrite(chns[j],dutys[i+j])  
                        # lights up the LEDs
                    time.sleep_ms(delayTimes)
        if(order ==0):
            while True:
                for i in range(0,16):
                    if not buttonRightToLeft.value(): 
                        # direction change
                        lightUp(1)
                    for j in reversed(range(0,8)):
                        mypwm.ledcWrite(chns[7-j],dutys[i+j]) 
                        # lights up the LEDs
                    time.sleep_ms(delayTimes)
try:
    # give it the first go by pressing one of these buttons
    while True:
        if not buttonLeftToRight.value():
            time.sleep_ms(20)
            lightUp(0)
        if not buttonRightToLeft.value():
            time.sleep_ms(20)
            lightUp(1)
except:
    mypwm.deinit()