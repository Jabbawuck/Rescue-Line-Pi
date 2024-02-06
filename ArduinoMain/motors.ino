////////////////////[Libraries]////////////////////
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
/////////////////////////////////////////////////////



//motorenpins
int motorR1 = A1;
int motorR2 = A2;
int motorL1 = A3;
int motorL2 = A4;
/////////////////////////////////////////////////////

void forward(){
  digitalWrite(motorR1, HIGH);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorL2, LOW);
}

void backward(){
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, HIGH);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, HIGH);
}

void right(){
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, HIGH);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorL2, LOW);
}

void left(){
  digitalWrite(motorR1, HIGH);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, HIGH);
}

void stop(){
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);
}

//////////[Motorentest]//////////////////////////
void motorentest(){
  forward(1000);
  stop(1000);
  right(90);
  forward(1000);
  stop(1000);
  backwards(1000);
  left(90);
  backwards(1000);
}
//////////////////////////////////////////////  

  
  
