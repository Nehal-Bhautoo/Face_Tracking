"""
    Resize an image
"""

import cv2
import numpy as np

image = cv2.imread('resources/car.jpg')
print("Original size: ", image.shape)
imgResize = cv2.resize(image, (1200, 800))
print("Resize: ", imgResize.shape)

cv2.imshow("Car", imgResize)
cv2.waitKey(0)
