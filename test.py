import time
from machine import Pin,PWM

class myPWM():
    def __init__(self, pwm0: int=15, pwm1: int=2, pwm2: int=0, pwm3: int=4, pwm4: int=5, pwm5: int=18, pwm6: int=19, pwm7: int=21):
        self._pwm0=PWM(Pin(pwm0),10000)
        self._pwm1=PWM(Pin(pwm1),10000)
        self._pwm2=PWM(Pin(pwm2),10000)
        self._pwm3=PWM(Pin(pwm3),10000)
        self._pwm4=PWM(Pin(pwm4),10000)
        self._pwm5=PWM(Pin(pwm5),10000)
        self._pwm6=PWM(Pin(pwm6),10000)
        self._pwm7=PWM(Pin(pwm7),10000)
        
    def ledcWrite(self,chn,value):
        if chn==0:
            self._pwm0.duty(value)
        elif chn==1:
            self._pwm1.duty(value)
        elif chn==2:
            self._pwm2.duty(value)
        elif chn==3:
            self._pwm3.duty(value)
        elif chn==4:
            self._pwm4.duty(value)
        elif chn==5:
            self._pwm5.duty(value)
        elif chn==6:
            self._pwm6.duty(value)
        elif chn==7:
            self._pwm7.duty(value)
    
    def deinit(self):
        self._pwm0.deinit()
        self._pwm1.deinit()
        self._pwm2.deinit()
        self._pwm3.deinit()
        self._pwm4.deinit()
        self._pwm5.deinit()
        self._pwm6.deinit()
        self._pwm7.deinit()


mypwm = myPWM(15,2,0,4,5,18,19,21)
chns=[0,1,2,3,4,5,6,7]
dutys=[0,0,0,0,0,0,0,0,1023,512,256,128,64,32,16,8,0,0,0,0,0,0,0,0]
delayTimes=50


buttonRightToLeft = Pin(13, Pin.IN,Pin.PULL_UP) 
buttonLeftToRight = Pin(14, Pin.IN,Pin.PULL_UP) 

def lightUp(order):
        if(order ==1):
            while True:
                for i in range(0,16):
                    # if not buttonLeftToRight.value():
                    #     lightUp(0)
                    for j in range(0,8):
                        mypwm.ledcWrite(chns[j],dutys[i+j])
                    time.sleep_ms(delayTimes)
        if(order ==0):
            while True:
                for i in range(0,16):
                    # if not buttonRightToLeft.value():
                    #     lightUp(1)
                    for j in reversed(range(0,8)):
                        mypwm.ledcWrite(chns[7-j],dutys[i+j])
                    time.sleep_ms(delayTimes)


while True:
    if not buttonLeftToRight.value():
        time.sleep_ms(20)
        lightUp(0)
    if not buttonRightToLeft.value():
        time.sleep_ms(20)
        lightUp(1)
    for i in range(0,16):
                    # if not buttonLeftToRight.value():
                    #     lightUp(0)
                    for j in range(0,8):
                        mypwm.ledcWrite(chns[j],dutys[i+j])
                    time.sleep_ms(delayTimes)



