////////////////////[Libraries]////////////////////
#include <SPI.h>
#include <Wire.h>
/////////////////////////////////////////////////////
//motorenpins
int motorR1 = 7;
int motorR2 = 8;
int motorL1 = 9;
int motorL2 = 10;
int motorSpeedPinR = 5;
int motorSpeedPinL = 6;

int defaultSpeed = 50; //Geschwindigkeit 0% bis 100%
int topSpeed = 150; //Maximalgeschwindigkeit
/////////////////////////////////////////////////////
//[allg. Motoren]/// 

void startMotors(){
  pinMode(motorR1, OUTPUT);
  pinMode(motorR2, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT);
  pinMode(motorSpeedPinL, OUTPUT);
  pinMode(motorSpeedPinR, OUTPUT);
}

void forward(int time, int speed){
  analogWrite(motorSpeedPinL, map(speed, 0, 100, 0, 255));
  analogWrite(motorSpeedPinR, map(speed, 0, 100, 0, 255));
  digitalWrite(motorR1, HIGH);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorL2, LOW);
  delay(time);
}

void backward(int time, int speed){
  analogWrite(motorSpeedPinL, map(speed, 0, 100, 0, 255));
  analogWrite(motorSpeedPinR, map(speed, 0, 100, 0, 255));
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, HIGH);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, HIGH);
  delay(time);
}

void left(int time, int speed){
  analogWrite(motorSpeedPinR, map(speed, 0, 100, 0, 255));
  analogWrite(motorSpeedPinL, map(speed, 0, 100, 0, 255));
  digitalWrite(motorR1, HIGH);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);
  delay(time);
}

void right(int time, int speed){
  analogWrite(motorSpeedPinR, map(speed, 0, 100, 0, 255));
  analogWrite(motorSpeedPinL, map(speed, 0, 100, 0, 255));
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorL2, LOW);
  delay(time);
}

void stop(int time){
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);
  delay(time);
}

void smoothDrive(int speed, int direction){
  analogWrite(motorSpeedPinR, map(direction, 90, -90, 0, topSpeed));
  analogWrite(motorSpeedPinL, map(direction, -90, 90, 0, topSpeed));
  digitalWrite(motorR1, HIGH);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, HIGH);
  digitalWrite(motorL2, LOW);
  //Serial.print(map(direction, 90, -90, 0, 255));
  //Serial.print(map(direction, -90, 90, 0, 255));
}

//////////////////////////////////////////////
//[Motorentest]///

void motorentest(){
  forward(1000, defaultSpeed);
  stop(1000);
  right(90, defaultSpeed);
  forward(1000, defaultSpeed);
  stop(1000);
  backward(1000, defaultSpeed);
  left(90, defaultSpeed);
  backward(1000, defaultSpeed);
}

void setup(){
  Serial.begin(115200);
  Serial.write("Arduino Serial opened");
  startMotors();
}
int turn = 0;
void loop(){
  //readOrientation();
  if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');
        if (data.startsWith("toino")) {
            turn = data.substring(5).toInt();
            // Save the value to an integer variable
            return turn;
        }
        return turn;
    }
  smoothDrive(topSpeed, turn);
  //Serial.println("test123");
}
  
