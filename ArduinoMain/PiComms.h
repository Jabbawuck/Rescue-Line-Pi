#ifndef PiComms_h
#define PiComms_h
#include "Arduino.h"

class PiComms
{
public:
    void begin();
    char[] read();
    void write();
private:
    bool _connected;
    int _msgLength;
    char[] receivedMsg;
    char[] sendMsg;
};

#endif