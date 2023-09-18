
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