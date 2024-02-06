////////////////////[Libraries]////////////////////
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>

//für BNO055 Sensor 
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
/////////////////////////////////////////////////////
//motorenpins
int motorR1 = A1;
int motorR2 = A2;
int motorL1 = A3;
int motorL2 = A4;

int defaultSpeed = 50 //Geschwindigkeit 0% bis 100%
/////////////////////////////////////////////////////
//[allg. Motoren]/// 

void startMotors(){
  pinMode(motorR1, OUTPUT);
  pinMode(motorR2, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT);
}

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

//////////////////////////////////////////////
//[Motorentest]///

void motorentest(){
  forward(1000, defaultSpeed);
  stop(1000);
  right(90, defaultSpeed);
  forward(1000, defaultSpeed);
  stop(1000);
  backwards(1000, defaultSpeed);
  left(90, defaultSpeed);
  backwards(1000, defaultSpeed);
}
//////////////////////////////////////////////  
//[allg. Gyro]///

void readOrientation(){
  sensors_event_t orientationData , angVelocityData , linearAccelData; //Winkeldaten
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);

  yawAngle =orientationData.orientation.x;
  pitchAngle = map(orientationData.orientation.y, 100, 0, -100, 0);
  rollAngle = orientationData.orientation.z;

  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);//Beschleunigungsdaten
  xAccel = linearAccelData.acceleration.x * 100;
  yAccel = linearAccelData.acceleration.y * 100;
  zAccel = linearAccelData.acceleration.z * 100;

}
///////////////////////////////////////////////

void setup(){
  Serial.begin(9600);
  startMotors();
  !bno.begin();
}

void loop(){
  readOrientation();
  motorentest();
}
  
