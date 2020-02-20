int potPin = A5;  // analog pin for the potentiometer
int val;    // variable to read the value from potentiometer

void setup() {
  pinMode(potPin,INPUT);
  Serial.begin(9600);
}

void loop() {
  val = analogRead(potPin);            // reads the value of the potentiometer (value between 0 and 1023)
  Serial.println(val);                 // print it to the serial monitor
}
