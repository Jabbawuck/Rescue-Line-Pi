#include "Arduino.h"
#include "PiComms.h"

void PiComms::PiComms()
{
    bool connected = false;
    int stringLength;
    string[] recievedMsg;
    string[] sendMSG;
}

void PiComms::begin()
{
    Serial.begin(19200);
    while(connected != true){
        if (Serial.available() > 0)
        {
            connected = true;
            stringLegth = Serial.Read();
        }
        
    }
}

void PiComms::read()
{
    Serial.readBytesUntil(\n, recievedMsg);
}

void PiComms::write()
{
    if(sendMsg.length < Serial.availableForWrite())
    Serial.write(sendMsg);
}