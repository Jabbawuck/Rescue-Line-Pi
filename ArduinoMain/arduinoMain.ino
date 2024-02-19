#include <Arduino.h> // Include the Arduino library

void setup(){
    Serial.begin(9600);
}
int turn;
void loop(){
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');
        command.trim();
        if (data.startsWith("toino")) {
            turn = data.substring(5).toInt();
            // Save the value to an integer variable
        }
    }
    
}
