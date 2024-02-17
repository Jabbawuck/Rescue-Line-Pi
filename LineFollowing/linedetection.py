import cv2
import numpy as np
import utilis

'''def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([0,0,0])
    upperWhite = np.array([179,255,255])
    masWhite = cv2.inRange(imgHsv,lowerWhite,upperWhite)
    return maskWhite

 '''



def track_black_line():
   
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
