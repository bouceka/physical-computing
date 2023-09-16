
#define PIN_LED 2
#define PIN_BUTTON_ON 13
#define PIN_BUTTON_OFF 12
// the setup function runs once when you press reset or power the board
void setup()
{
    // initialize digital pin PIN_LED as an output.
    pinMode(PIN_LED, OUTPUT);
    pinMode(PIN_BUTTON_ON, INPUT);
    pinMode(PIN_BUTTON_OFF, INPUT);
}

// the loop function runs over and over again forever
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