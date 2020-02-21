#include <Servo.h>

int potPin = A5;  // analog pin for the potentiometer
int val;    // variable to read the value from potentiometer
int servoPin = 9;

Servo myservo;

void setup() {
  pinMode(potPin,INPUT);
  Serial.begin(9600);
  myservo.attach(servoPin);
}

void loop() {
  val = analogRead(potPin);            // reads the value of the potentiometer (value between 0 and 1023)
  //Serial.println(val);                 // print it to the serial monitor
  val = map(val, 0, 1023, 0, 180);
  Serial.println(val);
  myservo.write(val);
  delay(15);
}
