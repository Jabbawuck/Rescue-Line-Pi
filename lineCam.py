import cv2
from picamera2 import Picamera2
import numpy as np
import time
import utility
import serial

thres = 0.45  # Threshold to detect object

picam = Picamera2()
turn = 0

if __name__ == "__main__":
    picam.start()
    utility.arduinoSerialCom()
    ser = serial.Serial(utility.detect_arduino_port(), 115200)
    fps_time = time.perf_counter()
    counter = 0
    fps =0
    
    camera_width = 640
    camera_height = 480
    while True:
        #picam.capture_file("videostream.jpg")
        #img = cv2.imread("videostream.jpg", -1)
        img = picam.capture_array()
        original_img = img
        img = cv2.resize(img, (camera_width, camera_height))
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        utility.showBlackMask(img)
        result = utility.track_line(img)
        
        counter += 1
        if time.perf_counter() - fps_time > 1:
            fps = int(counter / (time.perf_counter() - fps_time))
            fps_time = time.perf_counter()
            counter = 0
        cv2.putText(result, str(fps), (int(camera_width * 0.92), int(camera_height * 0.05)), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0),  1, cv2.LINE_AA)
        cv2.imshow('Line Tracking', result)
        sendMessage = "toino" + str(turn)
        ser.write(sendMessage.encode())
        utility.showGreenMask(original_img)
        green_result = utility.trackGreenDot(original_img)
        #green_track_result = track_green_color(img)
        cv2.imshow('Green Color Tracking', green_result)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
