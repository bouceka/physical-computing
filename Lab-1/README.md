# Physical Computing - LEDs and Push Buttons

In this laboratory, we will do simple circuits where we get more familiar with ESP32 and Python. Instructions are given by [Andrew J. Park, Ph.D.](https://www.twu.ca/profile/andrew-park).

We will use Freenove Ultimate Starter Kit for ESP32-WROVER which you can buy on [Amazon](https://www.amazon.ca/ESP32-WROVER-Contained-Compatible-Bluetooth-Tutorials/dp/B08FM2NCST). How to set up the kit and start uploading code you can find on [Freenove](https://www.freenove.com/tutorial).

## Project 1 - Three LEDs

### Date: 09/16/23

![Three LEDs image](https://res.cloudinary.com/boucekdev/image/upload/v1695062876/github/fitngwzptsagqj3a9vy7.jpg)

### Instructions:

Design and construct a circuit that includes three LEDs (red, green, and blue). When your program
runs, each LED turns on and off (blinks) sequentially and continually (red → green → blue → red → green → blue → …). Capture your settings and working circuit in photos and videos.

### Parts:

- ESP32-WROVER x1
- GPIO Extension Board x1 (optional)
- Breadboard x1
- Jumper M/M x6
- Green LED 1x
- Red LED 1x
- Blue LED 1x
- Resistor 220Ω x3

### Three LEDs schema:

![Three LEDs Schematic image](https://res.cloudinary.com/boucekdev/image/upload/v1695062876/github/fod6vowxeatjtmuk0s4c.jpg)

### Three LEDs Breadboard View:

![Three LEDs Breadboard View image](https://res.cloudinary.com/boucekdev/image/upload/v1695062876/github/o1gpbc6bjdh9em4jzmoh.jpg)

### Source Code:

```python
from time import sleep_ms
from machine import Pin

ledGreen=Pin(2,Pin.OUT)
ledBlue=Pin(15,Pin.OUT)
ledRed=Pin(18,Pin.OUT)
arr = [ledBlue, ledGreen, ledRed]

try:
    while True:
        for element in arr:
            element.value(1)
            sleep_ms(200)
            element.value(0)

except KeyboardInterrupt:
    pass
```

![Three LEDs gif](https://res.cloudinary.com/boucekdev/image/upload/v1695095256/github/xqr54kfhulvuevkerb2x.gif)

## Project 2 - Two push buttons and an LED

### Date: 09/16/23

![Two push buttons image](https://res.cloudinary.com/boucekdev/image/upload/v1695062863/github/kofupmaymaicfucg2k8c.jpg)

### Instructions:

Design and construct a circuit that includes two push buttons and an LED. When one button is pushed, the LED is on while the other button is pushed, the LED is off. When the same button is pushed multiple times, it should not change the status of the LED. Capture your settings and working circuit in photos and videos.

### Parts:

- ESP32-WROVER x1
- GPIO Extension Board x1 (optional)
- Breadboard x1
- Jumper M/M x6
- Green LED 1x
- Push buttons 2x
- Resistor 220Ω x1
- Resistor 10kΩ x4

### Two push buttons schema:

![Two push buttons Schematic image](https://res.cloudinary.com/boucekdev/image/upload/v1695062863/github/gel1uit48joskh04gzpm.jpg)

### Two push buttons Breadboard View:

![Two push buttons Bread View image](https://res.cloudinary.com/boucekdev/image/upload/v1695062863/github/ljbtiy8zgqvz2xzdkfxr.jpg)

### Source Code:

```python
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

```

### Result:

![Two push buttons gif](https://res.cloudinary.com/boucekdev/image/upload/v1695095267/github/hni9hdlgglxnft9cpq51.gif)

Blog Link: https://www.boucek.dev/blog/physical-computing-LEDs-and-push-buttons
