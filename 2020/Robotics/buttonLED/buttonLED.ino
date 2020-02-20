/*
   This code uses a button to control the status of an LED. It only works some of the time
   because it can mistake a single button push for multiple button presses. The debounce example
   fixes this issue by ignoring any additional button presses within 50 milliseconds.
*/

const int buttonPin = 8;    // the number of the pushbutton pin
const int ledPin = 7;      // the number of the LED pin

// This code is run once
void setup() {
  pinMode(buttonPin, INPUT); // Use the button as an input
  pinMode(ledPin, OUTPUT); // Use the LED as an output

  // set initial LED state
  digitalWrite(ledPin, LOW); // Turn the LED off
  Serial.begin(9600); // Open up a connection with the serial monitor (allows us to send or receive text from the Arduino)
}

// This code is run repeatedly until the Arduino loses power
void loop() {
  int reading = digitalRead(buttonPin); // Read the status of the button. It's either HIGH (pushed) or LOW (not pushed).
  if (reading == HIGH) { // If button is pushed
    if (ledStatus == LOW) { // and the LED is off
      digitalWrite(ledPin, HIGH); // turn the LED on
    } else { // if the LED is on
      digitalWrite(ledPin, LOW); // turn the LED off
    }
  }

}
