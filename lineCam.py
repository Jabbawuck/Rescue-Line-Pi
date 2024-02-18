import cv2
from picamera2 import Picamera2
import numpy as np

thres = 0.45 # Threshold to detect object

resolution = (640, 480)
frame_rate = 30

picam = Picamera2()

def track_line(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, thresholded = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_External, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            
            x, y, w, h = cv2.boundingRect(contour)
            
            cv2.rectangle(image, (x, y), (x +w , y + h), (0, 255, 0), 2)
            
            center_x = x + w // 2
            center_y = y + h // 2
            
            cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)
            
            image_center_x, _ = image.shape[1] // 2, image.shape[0] // 2
            if center_x < image_center_x:
                print("Line is on the left")
            elif center_x > image_center_x:
                print("Line is on the right")
            else:
                print("Line is in the center")
                
    return image
    
imgBgr = cv2.imread('videostream.jpg')


    
def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([87, 87, 87])
    maskBlack = cv2.inRange(imgHsv,lower_black,upper_black)
    return maskBlack
    
    
def getLaneCurve(img):

    imgThres = thresholding(img)

    cv2.imshow('Thres',imgThres)
    return None

if __name__ == "__main__":
	cap = cv2.VideoCapture('videostream.jpg')


	picam.start()

	while True:
		picam.capture_file("videostream.jpg")
		img = cv2.imread("videostream.jpg", -1)
		#success, img = cap.read()
		getLaneCurve(img)
        
		cv2.imshow("Output",img)
		cv2.waitKey(1)
'''    
	while True:
		ret, frame = cap.read()
		if not ret:
			break
        
        
		result =track_line(frame)
		cv2.imshow('Line Tracking', result)
    
		if cv2.waitKey(1) & OxFF == ord('q'):
			break
        '''
        


cap = cv2.VideoCapture(0)




cap.release()
cv2.destroyAllWindows()

