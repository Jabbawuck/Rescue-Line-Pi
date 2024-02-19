import cv2
import numpy as np
import utlis 

def getLaneCurve(img):

    imgThres = utlis.thresholding(img)

    cv2.imshow('Thres',imgThres)
    return None



if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    while True:
        success, img = cap.read()
        getLaneCurve(img)

        cv2.imshow('vid',img)
        cv2.waitKey(1) 