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

