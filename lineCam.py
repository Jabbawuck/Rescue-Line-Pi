import cv2
from picamera2 import Picamera2
import numpy as np
import time
import utility
import serial

thres = 0.45  # Threshold to detect object

picam = Picamera2()
turn = 0

def track_line(image):
    global turn
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center_x = x + w // 2
            center_y = y + h // 2
            image_center_x, _ = image.shape[1] // 2, image.shape[0] // 2
            if center_x > image_center_x - 50 and center_x < image_center_x + 50:
                if turn > 0:
                    turn -= 1
                if turn < 90:
                    turn += 1
                print("Line is in the center    " + str(turn))
            elif center_x < image_center_x:
                if turn > -90:
                    turn -= 1
                print("Line is on the left      " + str(turn))
            elif center_x > image_center_x:
                if turn < 90:
                    turn += 1
                print("Line is on the right     " + str(turn))
            
    return image




def getLaneCurve(img):
    imgThres = utility.thresholding(img)
    cv2.imshow('Thres', imgThres)
    return None


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
        getLaneCurve(img)
        result = track_line(img)
        
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
        
