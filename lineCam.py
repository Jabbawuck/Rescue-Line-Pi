import cv2
from picamera2 import Picamera2


thres = 0.45 # Threshold to detect object

picam = Picamera2()

if __name__ == "__main__":


    picam.start()

    while True:
        picam.capture_file("videostream.jpg")
        img = cv2.imread("videostream.jpg", -1)
        
        cv2.imshow("Output",img)
        cv2.waitKey(1)

