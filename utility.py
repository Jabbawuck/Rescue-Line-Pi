import cv2
import numpy as np
import time
import serial
import glob

turn = 0

def detect_arduino_port():
    """
    Detects the Arduino port by listing all the serial ports and trying to open each port.
    If a port is successfully opened, it is closed and returned.
    If no port is found, None is returned.
    """
    ports = glob.glob('/dev/ttyUSB*')
    for port in ports:
        try:
            ser = serial.Serial(port, 115200)
            ser.close()
            return port
        except serial.SerialException:
            pass
    return None

def arduinoSerialCom():
    """
    Tries to find the Arduino port 10 times by calling the 'detect_arduino_port' function.
    If a port is found, it is opened and its name is printed.
    If no port is found after 10 attempts, an error message is printed.
    """
    for x in range(10):
        arduino_port = detect_arduino_port()
        if arduino_port:
            ser = serial.Serial(arduino_port, 115200)
            print("Arduino found at", arduino_port)
            return arduino_port
        else:
            print("Error: Arduino not found.")
            time.sleep(1)

#Linetracking
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

def thresholding(input_image):
    """
    Performs thresholding on the input image.
    Converts the image to HSV color space and applies a black color range threshold.
    Returns the thresholded image.
    """
    imgHsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([87, 87, 87])
    maskBlack = cv2.inRange(imgHsv, lower_black, upper_black)
    return maskBlack

def showBlackMask(img):
    imgThres = thresholding(img)
    cv2.imshow('Thres', imgThres)
    return None



#Green dot tracking methods

def trackGreenColor(fullcolor_input_image):
    """
    Tracks green color in the input image.
    Converts the image to HSV color space and applies a green color range threshold.
    Returns the binary mask of the green color.
    """
    hsv = cv2.cvtColor(fullcolor_input_image, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([20, 80, 60])
    upper_green = np.array([80, 255, 255])
    maskGreen = cv2.inRange(hsv, lower_green, upper_green)
    return maskGreen


# give me the coords pls not the relative position to center
def trackGreenDot(img):
    """
    Tracks green Dots in the input image.
    Converts the image to binary mask using the 'trackGreenColor' function.
    Finds contours in the binary mask and draws bounding boxes around the detected green Dots.
    Determines the position of the green Dots relative to the image center.
    Prints the position of the green Dots.
    Returns the image with bounding boxes drawn.
    """
    contours_green, _ = cv2.findContours(trackGreenColor(img), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > 10:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            center_x = x + w // 2
            image_center_x, _ = img.shape[1] // 2, img.shape[0] // 2
            if center_x < image_center_x:
                print("Dot is on the left")
            elif center_x > image_center_x:
                print("Dot is on the right")
            else:
                print("No Dot detected")
    return img

def showGreenMask(img):
    """
    Displays the green Dots mask in a separate window.
    Converts the image to binary mask using the 'trackGreenColor' function.
    Displays the binary mask in a separate window.
    """
    imgGT = trackGreenColor(img)
    cv2.imshow('Box', imgGT)
    return None
    
        