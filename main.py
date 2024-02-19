import serial
import glob
import time
import RPi.GPIO as GPIO
import subprocess

# Function to detect Arduino port
def detect_arduino_port():
    # List all serial ports
    ports = glob.glob('/dev/ttyUSB*')
    # Iterate over the ports
    for port in ports:
        try:
            # Try to open the port
            ser = serial.Serial(port, 9600)
            # If the port is open, close it and return the port
            ser.close()
            return port
        except serial.SerialException:
            # If the port is not open, continue to the next port
            pass
    # If no port is found, return None
    return None

# Function to restart the script
def restart_script(channel):
    subprocess.call(['python3', '/home/gbg/Jabbawuck/Rescue-Line-Pi/main.py'])

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=restart_script, bouncetime=300)

# Get the Arduino port
for x in range(10):
    arduino_port = detect_arduino_port()

    # If a port is found, open it
    if arduino_port:
        ser = serial.Serial(arduino_port, 9600)
        print("Arduino found at", arduino_port)
        time.sleep(3)
        exit
    # If no port is found, print an error message
    else:
        print("Error: Arduino not found.")
        time.sleep(1)

message_to_send = "Hello, Arduino!"
while True:
    # Send the message from the main module over the serial port
    ser.write(message_to_send.encode())
