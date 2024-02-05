#ifndef PiComms_h
#define PiComms_h

#include "Arduino.h"

#define MAX_MSG_LENGTH 5

class PiComms
{
public:
    PiComms();
    void begin();
    char read(char* buffer, int bufferSize);
    void write(const char* sendMsg);

private:
    bool _connected;
    int _msgLength;
    char receivedMsg[MAX_MSG_LENGTH];
    char sendMsg[MAX_MSG_LENGTH];
};

#endif
