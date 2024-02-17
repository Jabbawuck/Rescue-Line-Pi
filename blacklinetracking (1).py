import cv2
import numpy as np

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

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
        
    result =track_line(frame)
    cv2.imshow('Line Tracking', result)
    
    if cv2.waitKey(1) & OxFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
