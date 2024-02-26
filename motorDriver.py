from gpiozero import Motor, PWMLED

#driving variables
fastTurnThreshold = 45

#Gpio pins
#motorPins
in1 = 13 #Physical pin 33
in2 = 19 #Physical pin 35
in3 = 26 #Physical pin 37
in4 = 16 #Physical pin 36
enA = 20 #Physical pin 38
enB = 21 #Physical pin 40

motorLeft = Motor(in1, in2) #motorLeft.forward() or motorLeft.backward() or motorLeft.stop()
motorRight = Motor(in3, in4)
speedLeft = PWMLED(enA) #speed can be controlled with speedLeft.value = x where x is a float between 0 and 1
speedRight = PWMLED(enB)

def smoothDrive(speed, direction):
    if direction >= -fastTurnThreshold and direction <= fastTurnThreshold: #when the direction is not that hard turns normally
        motorLeft.forward()
        motorRight.forward()
        speedLeft.value = speed * map(direction, -fastTurnThreshold, 0, 1, 0) #might work... who knows really
        speedRight.value = speed * map(direction, 0, fastTurnThreshold, 0, 1)
    if direction < -fastTurnThreshold or direction > fastTurnThreshold: #when the direction is a hard turn
        if direction < -90: #when the direction is a hard hard left
            motorLeft.backward()
            motorRight.forward()
            speedLeft.value = map(direction, -180, -90, 1, 0)
            speedRight.value = speed * (map(direction, 0, -180, 0, 1)^3)
        if direction > 90: #when the direction is a hard hard right
            motorLeft.forward()
            motorRight.backward()
            speedLeft.value = speed * (map(direction, 0, 180, 0, 1)^3)
            speedRight.value = map(direction, 180, 90, 1, 0)
        else:
            motorLeft.forward()
            motorRight.forward()
            speedLeft.value = speed * (map(direction, -fastTurnThreshold, 0, 1, 0)^2) #again rather unsure about this
            speedRight.value = speed * (map(direction, 0, fastTurnThreshold, 0, 1)^2)

def driveLoopCallable(speed, direction):
    smoothDrive(speed, direction)