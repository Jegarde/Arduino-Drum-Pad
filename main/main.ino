const int buttonCount = 8;
int buttonPins[buttonCount] = {2, 4, 6, 8, 3, 5, 7, 9};
int buttonStates[buttonCount] = {};
int lastButtonStates[buttonCount] = {};

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  initializeButtons();
  Serial.begin(9600);
}

void initializeButtons() {
  for (int i = 0; i < buttonCount; i++) {
    int buttonPin = buttonPins[i];
    pinMode(buttonPin, INPUT_PULLUP);

    // Prevent first time false positives
    buttonStates[i] = digitalRead(buttonPin);
    lastButtonStates[i] = buttonStates[i];
  }
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    int buttonPin = buttonPins[i];
    int reading = digitalRead(buttonPin);

    if (reading != lastButtonStates[i]) {
      lastDebounceTime = millis();
    }

    if ((millis() - lastDebounceTime) > debounceDelay) {
      if (reading != buttonStates[i]) {
        buttonStates[i] = reading;

        if (reading == LOW) {
          Serial.print(buttonPin);
          Serial.println(" is pressed.");
        } else {
          Serial.print(buttonPin);
          Serial.println(" is released.");
        }
      }
    }

    lastButtonStates[i] = reading;
  }
}
