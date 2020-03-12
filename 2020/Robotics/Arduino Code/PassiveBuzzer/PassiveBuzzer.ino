#include <pitches.h>
 
// notes in the melody (C Major Scale:
int melody[] = {
  NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6};
int duration = 500;  // Note will play for half a second
int buzzerPin = 8;

void setup() {
 pinMode(buzzerPin,OUTPUT);
}
 
void loop() {  
  for (int thisNote = 0; thisNote < 8; thisNote++) {
    // Make the sound for 0.5 seconds
    tone(buzzerPin, melody[thisNote], duration);

    // Delay for 1 second
    delay(1000);
  }
   
  // restart after two seconds 
  delay(2000);
}
