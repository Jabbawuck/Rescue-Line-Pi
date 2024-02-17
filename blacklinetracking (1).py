import cv2
import numpy as np
from picamera2 import Picamera2 
from libcamera import controls
import os
import time 

camera_x = 640
camera_y = 480

camera = Picamera2()

mode = camera.sensor_modes[0]
camera.configure(camera.create_video_configuration(sensor={'output_size': mode['size'], 'bit_depth': mode['bit_depth']}))
camera.start()


camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 6.5 , "FrameDurationLimits": (1000000 // 50, 1000000 // 50)})
time.sleep(0.1)

while True: 
    raw_capture = camera.capture_array()
    #raw_capture = cv2.resize(raw_capture, (camera_x, camera_y))
    cv2_img = cv2.cvtColor(raw_capture, cv2.COLOR_RGB2BGR)
    cv2.imshow('test', cv2_img)

''' def track_black_line():
   
    cap = cv2.VideoCapture(0)

    while True:
     
        ret, frame = cap.read()

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to separate black line from background
        _, thresholded = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours on the original frame
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        
        cv2.imshow('Black Line Tracker', frame)

        # Check for key press
        key = cv2.waitKey(1)
        if key == 27:  # If 'Esc' is pressed, exit
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_black_line()
'''
