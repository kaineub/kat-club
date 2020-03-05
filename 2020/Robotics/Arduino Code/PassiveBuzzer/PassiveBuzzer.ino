#include <_______>
 
// notes in the melody:
int melody[] = {
  NOTE_C5, NOTE_D5, NOTE_E5, NOTE_F5, NOTE_G5, NOTE_A5, NOTE_B5, NOTE_C6};
int duration = _________;  // Note will play for half a second
int buzzerPin = ____________

void setup() {
 pinMode(buzzerPin,_____);
}
 
void loop() {  
  for (int thisNote = 0; thisNote < 8; thisNote++) {
    // pin8 output the voice, every scale is 0.5 sencond
    tone(______, melody[thisNote], duration);

    // Delay for 1 second
    delay(_____);
  }
   
  // restart after two seconds 
  delay(________);
}
