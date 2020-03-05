#include <SR04.h> // Import the SR04 library

int trigPin = 12; // Trigger pin on the arduino
int echoPin = 11; // Echo pin on the arduino
long distance; // Variable for the distance detected

SR04 sensor = SR04(echoPin,trigPin); // Create a SR04 (ultrasonic sensor) object

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // Open a connection to the serial monitor
}

void loop() {
  // put your main code here, to run repeatedly:
  distance = sensor.Distance(); // Detect the distance
  Serial.print(distance); // Print the distance to the serial monitor (without going to a newline after)
  Serial.println("cm"); // Print cm after the distance and then go to a new line
  delay(1000); // Delay by one second between measurements
}
