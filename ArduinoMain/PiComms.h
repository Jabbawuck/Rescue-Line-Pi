#ifndef PiComms_h
#define PiComms_h
#include "Arduino.h"

class PiComms
{
public:
    void begin();
    void read();
    void write();
};

#endif