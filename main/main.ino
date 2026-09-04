#include "pitches.h"

const int BUZZER_PIN = 10;

const int BUTTON_COUNT = 8;
int buttonPins[BUTTON_COUNT] = {2, 4, 6, 8, 3, 5, 7, 9};
int buttonStates[BUTTON_COUNT] = {};
int lastButtonStates[BUTTON_COUNT] = {};

int notes[BUTTON_COUNT] = {NOTE_B5, NOTE_C6, NOTE_D6, NOTE_E6, NOTE_F6, NOTE_G6, NOTE_A6, NOTE_B6};

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
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

    if ((millis() - lastDebounceTime) > debounceDelay) {
      if (reading != buttonStates[i]) {
        buttonStates[i] = reading;

        if (reading == LOW) {
          tone(BUZZER_PIN, notes[i], 100);
          Serial.print(i);
          Serial.println(" is pressed.");
        } else {
          Serial.print(i);
          Serial.println(" is released.");
        }
      }
    }

    lastButtonStates[i] = reading;
  }
}
