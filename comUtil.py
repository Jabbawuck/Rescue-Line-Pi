import serial.tools.list_ports

ports = serial.tools.list_ports.comports
serialInst = serial.Serial()

portlist = []

for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0, len(portlist)):
    if portlist[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open

def sendToArduino(message):
    """
    Sends a message to the Arduino.

    Args:
        message (str): The message to be sent.

    Returns:
        None
    """
    stringMessage = str(message)
    serialInst.write(stringMessage.encode('utf-8'))