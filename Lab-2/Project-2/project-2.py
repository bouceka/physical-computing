import neopixel
import time
from machine import Pin, PWM
from random import randint

pins = [15, 2, 0] 

pwm0 = PWM(Pin(pins[0]), 10000)  # Red
pwm1 = PWM(Pin(pins[1]), 10000)  # Green
pwm2 = PWM(Pin(pins[2]), 10000)  # Blue

buttonChangeColor = Pin(4, Pin.IN, Pin.PULL_UP)


def setColorRGB(r, g, b):
    pwm0.duty(1023 - r)
    pwm1.duty(1023 - g)
    pwm2.duty(1023 - b)


pin = Pin(5, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)

# colors from:
# https://docs.circuitpython.org/projects/led-animation/en/latest/api.html
# https://www.rapidtables.com/web/color/
brightness = 10
colors = [[255, 0, 0],  # red
          [255, 40, 0],  # orange
          [255, 150, 0],  # yellow
          [0, 255, 0],  # green
          [0, 0, 255],  # blue
          [75, 0, 130],  # indigo
          [238, 130, 218]]  # violet

colorIndex = 0
while True:
    while True:
        if not buttonChangeColor.value():
            time.sleep_ms(100) # giving time to the user
            colorIndex = (colorIndex + 1) % len(colors) # button iterate through the array
        for j in range(0, 8):
            np[j] = colors[colorIndex] # set color for the NEOPixel
            setColorRGB(colors[colorIndex][0]*4, colors[colorIndex]
                     [1]*4, colors[colorIndex][2]*4) # set color for the RGB
            np.write()
        time.sleep_ms(100)
