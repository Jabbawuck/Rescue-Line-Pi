from picamera2 import PiCamera2
from time import sleep
import cv2
import numpy as np
camera = PiCamera()


#camera test
camera.start_preview()
sleep(5)
"""camera.capture('/home/pi/Desktop/image.jpg')# takepicture; saved on desktop"""
camera.stop_preview()

camera.start_preview(alpha=200)# durchlässigkeit vom preview ; 0 bis 255

# videorecording
"""camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()"""


