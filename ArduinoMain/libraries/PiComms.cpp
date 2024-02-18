#include "PiComms.h"

PiComms::PiComms()
{
    _connected = false;
    _msgLength = 5;
}

void PiComms::begin()
{
    Serial.begin(19200);
    while (!_connected)
    {
        if (Serial.available() > 0)
        {
            _connected = true;
            _msgLength = Serial.read();
        }
    }
}

char PiComms::read(char* buffer, int bufferSize)
{
    Serial.readBytesUntil('\n', buffer, bufferSize);
    return buffer[5];
}

void PiComms::write(const char* sendMsg)
{
    if (strlen(sendMsg) < Serial.availableForWrite())
    {
        Serial.write(sendMsg, strlen(sendMsg));
    }
}
