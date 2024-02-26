import cv2
from picamera2 import Picamera2 as picam
import numpy as np
import time
import utility
import serial
#import comUtil
import motorDriver

thres = 0.45  # Threshold to detect object

#picam = Picamera2()
turn = 0

def main():
    """
    Main function to start the line tracking process.
    """
    picam.start()
    #utility.arduinoSerialCom()
    ser = serial.Serial(utility.detect_arduino_port(), 115200)
    fps_time = time.perf_counter()
    counter = 0
    fps = 0
    
    camera_width = 640
    camera_height = 480
    while True:
        # Capture image from the camera
        img = picam.capture_array()
        original_img = img
        
        # Resize and convert the image to BGR color space
        img = cv2.resize(img, (camera_width, camera_height))
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        
        # Show black mask on the image
        utility.showBlackMask(img)
        
        # Track the line on the image
        result = utility.track_line(img)
        
        counter += 1
        if time.perf_counter() - fps_time > 1:
            fps = int(counter / (time.perf_counter() - fps_time))
            fps_time = time.perf_counter()
            counter = 0
        
        # Display the FPS on the image
        cv2.putText(result, str(fps), (int(camera_width * 0.92), int(camera_height * 0.05)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0),  1, cv2.LINE_AA)
        cv2.imshow('Line Tracking', result)
        
        # Send message to Arduino
        #sendMessage = "toino" + str(turn)
        #comUtil.sendToArduino(sendMessage)
        
        # Show green mask on the original image
        utility.showGreenMask(original_img)
        
        # Track the green dot on the original image
        green_result = utility.trackGreenDot(original_img)
        cv2.imshow('Green Color Tracking', green_result)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()
    motorDriver.driveLoopCallable(10, utility.track_line())
        
