/*
  Modified version of Blink

  This code blinks an LED that is connected to pin 7 on the Arduino.
*/

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 7 as an output.
  pinMode(7, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(7, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second (1000 ms)
  digitalWrite(7, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second (1000 ms)
}
