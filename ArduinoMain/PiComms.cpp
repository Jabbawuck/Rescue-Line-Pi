#include "Arduino.h"
#include "PiComms.h"

PiComms::PiComms()
{
    bool _connected = false;
    int _msgLength;
    char[] receivedMsg;
    char[] sendMSG;
}

void PiComms::begin()
{
    Serial.begin(19200);
    while(_connected != true){
        if (Serial.available() > 0)
        {
            _connected = true;
            _msgLength = Serial.Read();
        }
        
    }
}

char[] PiComms::read()
{
    Serial.readBytesUntil("\n", receivedMsg);
    return receivedMsg;
}

void PiComms::write()
{
    if(sendMsg.length < Serial.availableForWrite())
    Serial.write(sendMsg);
}