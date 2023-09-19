import time
from machine import Pin

led = Pin(2, Pin.OUT)
buttonOn = Pin(13, Pin.IN, Pin.PULL_UP)
buttonOff = Pin(12, Pin.IN, Pin.PULL_UP)


def reverseGPIOON():
    led.value(1)

def reverseGPIOOFF():
    led.value(0)

while True:
    if not buttonOn.value():
        time.sleep_ms(20)
        reverseGPIOON()
    if not buttonOff.value():
        reverseGPIOOFF()
        time.sleep_ms(20)
