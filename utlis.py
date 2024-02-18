import cv2
import numpy as np

def thresholding(img):
    imageHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([30, 30, 30])
    maskBlack = cv2.inRange(imgHsv,lower_black,upper_black)
    return maskBlack