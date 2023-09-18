
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