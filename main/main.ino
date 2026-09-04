const int BUTTON_COUNT = 8;
int buttonPins[BUTTON_COUNT] = {3, 5, 7, 9, 2, 4, 6, 8}; // Bottom row to upper row
int buttonStates[BUTTON_COUNT] = {};
int lastButtonStates[BUTTON_COUNT] = {};

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 25;

void setup() {
  initializeButtons();
  Serial.begin(9600);
}

void initializeButtons() {
  for (int i = 0; i < BUTTON_COUNT; i++) {
    int buttonPin = buttonPins[i];
    pinMode(buttonPin, INPUT_PULLUP);

    // Prevent first time false positives
    buttonStates[i] = digitalRead(buttonPin);
    lastButtonStates[i] = buttonStates[i];
  }
}

void loop() {
  for (int i = 0; i < BUTTON_COUNT; i++) {
    int buttonPin = buttonPins[i];
    int reading = digitalRead(buttonPin);

    if (reading != lastButtonStates[i]) {
      lastDebounceTime = millis();
    }

    // Try to prevent false-positives with button presses 
    // with slight delay :(
    if ((millis() - lastDebounceTime) > debounceDelay) {
      if (reading != buttonStates[i]) {
        buttonStates[i] = reading;

        if (reading == LOW) {
          Serial.print("+");  // + prefix means pressed in listener
          Serial.println(i);
        } else {
          Serial.print("-");  // - prefix means released in listener
          Serial.println(i);
        }
      }
    }

    lastButtonStates[i] = reading;
  }
}
