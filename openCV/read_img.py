"""
    Read image
"""

import cv2
import numpy as np

# Read images from resource file
image = cv2.imread('resources/user.jpg')

kernel = np.ones((5, 5), np.uint8)

# convert image to gray scale
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# find edges in image
imgCanny = cv2.Canny(image, 150, 200)

# increase thickness of edges
imgDialation = cv2.dilate(imgCanny, kernel, iterations=5)

# make edges thinner
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Dialation", imgDialation)
cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)

