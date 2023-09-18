# Physical Computing - LEDs and Push Buttons

In this laboratory, we will do simple circuits where we get more familiar with ESP32 and using C++.

## Project 1 - Three LEDs

![Three LEDs image](./Project-1/project-1.jpg)

### Date: 09/16/23

Description: Design and construct a circuit that includes three LEDs (red, green, and blue). When your program
runs, each LED turns on and off (blinks) sequentially and continually (red → green → blue → red → green → blue → …). Capture your settings and working circuit in photos and videos.

### Parts:

- Jumper M/M x6
- 1 Green LED
- 1 Red LED
- 1 Blue LED
- Resistor 220Ω x3

### Three LEDs schema:

![Three LEDs Schematic image](./Project-1/project-1-schematic.jpg)

### Three LEDs Breadboard View:

![Three LEDs Breadboard View image](./Project-1/project-1-breadboard-view.jpg)

### Source Code:

```cpp
#define LED_GREEN  2
#define LED_BLUE  13
#define LED_RED  15

void setup() {
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_RED, OUTPUT);
}

void loop() {
    int leds[] = {LED_GREEN, LED_BLUE, LED_RED};

    for (int i = 0; i < 3; i++) {
      digitalWrite(leds[i], HIGH);
      delay(1000);
      digitalWrite(leds[i], LOW);
      delay(1000);
    }
}
```

![Three LEDs gif](./Project-1/project-1.gif)

## Project 2 - Two push buttons and an LED

![Two push buttons image](./Project-2/project-2.jpg)

### Date: 09/16/23

Description: Design and construct a circuit that includes two push buttons and an LED. When one button is pushed, the LED is on while the other button is pushed, the LED is off. When the same button is pushed multiple times, it should not change the status of the LED. Capture your settings and working circuit in photos and videos.

### Parts:

- Jumper M/M x6
- 1 Green LED
- 1 Two push buttons
- Resistor 220Ω x1
- Resistor 10kΩ x4

### Two push buttons schema:

![Two push buttons Schematic image](./Project-2/project-2-schematic.jpg)

### Two push buttons Breadboard View:

![Two push buttons Bread View image](./Project-2/project-2-breadboard-view.jpg)

### Source Code:

```cpp
#define PIN_LED 2
#define PIN_BUTTON_ON 13
#define PIN_BUTTON_OFF 12
void setup()
{
    pinMode(PIN_LED, OUTPUT);
    pinMode(PIN_BUTTON_ON, INPUT);
    pinMode(PIN_BUTTON_OFF, INPUT);
}

void loop()
{
    if (digitalRead(PIN_BUTTON_ON) == LOW)
    {
        delay(20);
        buttonOn(PIN_LED);
    }
    if (digitalRead(PIN_BUTTON_OFF) == LOW)
    {
        delay(20);
        buttonOff(PIN_LED);
    }
}

void buttonOff(int pin)
{
    digitalWrite(pin, LOW);
}
void buttonOn(int pin)
{
    digitalWrite(pin, HIGH);
}
```

### Result:

![Two push buttons gif](./Project-2/project-2.gif)
