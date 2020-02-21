#include <Servo.h>

int potPin = A5;  // analog pin for the potentiometer
int val;    // variable to read the value from potentiometer
int servoPin = 9; // pin that the servo is controlled from

Servo myservo; // Create an object that allows us to control the servomotor

// Runs once when the Arduino first turns on
void setup() {
  pinMode(potPin,INPUT); // Set the potentiometer pin as an input
  Serial.begin(9600); // Open a connection with the serial monitor
  myservo.attach(servoPin); // tell myservo which pin the servomotor is on
}

void loop() {
  val = analogRead(potPin);            // reads the value of the potentiometer (value between 0 and 1023)
  //Serial.println(val);                 // print it to the serial monitor
  val = map(val, 0, 1023, 0, 180);     // change the value from the potentiometer into a value between 0 and 180 (the servo can only rotate 180 degrees)
  Serial.println(val);                 // print that value to the serial monitor
  myservo.write(val);                  // tell the servo to move to the angle
  delay(15);                           // delay for 15 ms to allow the servo to move to that angle
}
