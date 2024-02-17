from picamera import PiCamera
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

"""def list_images(images, cols = 2, rows = 5, cmap=None):
    """
    Display a list of images in a single figure with matplotlib.
        Parameters:
            images: List of np.arrays compatible with plt.imshow.
            cols (Default = 2): Number of columns in the figure.
            rows (Default = 5): Number of rows in the figure.
            cmap (Default = None): Used to display gray images.
    """
    plt.figure(figsize=(10, 11))
    for i, image in enumerate(images):
        plt.subplot(rows, cols, i+1)
        #Use gray scale color map if there is only one channel
        cmap = 'gray' if len(image.shape) == 2 else cmap
        plt.imshow(image, cmap = cmap)
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout(pad=0, h_pad=0, w_pad=0)
    plt.show()"""

