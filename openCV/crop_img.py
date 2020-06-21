"""
    Crop an image
"""

import cv2

image = cv2.imread('resources/car.jpg')
imgCropped = image[0:800, 1000:1200]

cv2.imshow("Car", imgCropped)
cv2.waitKey(0)
