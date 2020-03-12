 /* These pins turn the motors on/off */
int ENA = 5;    // Left  wheel speed
int ENB = 6;    // Right wheel speed
/* These pins control the direction of the motors*/
int IN2 = 7;
int IN1 = 8;  
int IN3 = 9;
int IN4 = 11; 

//set car speed
int CAR_SPEED = 100;
typedef unsigned char u8;  //Change the name of unsigned char to u8

void forward(u8 car_speed)
{

  analogWrite(ENA, car_speed);
  analogWrite(ENB, car_speed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}


void back(u8 car_speed)
{

  analogWrite(ENA, car_speed);
  analogWrite(ENB, car_speed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}


void left(u8 car_speed)
{

  analogWrite(ENA, car_speed);
  analogWrite(ENB, car_speed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void right(u8 car_speed)
{
  analogWrite(ENA, car_speed);
  analogWrite(ENB, car_speed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void stop()
{
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);
}

void setup() {
  pinMode(IN1,OUTPUT);//before useing io pin, pin mode must be set first 
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
}

void loop() {
  back(CAR_SPEED);  //go forward
  delay(1000);
  forward(CAR_SPEED);
  delay(1000);
  left(CAR_SPEED);
  delay(1000);
  right(CAR_SPEED);
  stop();
  delay(1000);

}
