import cv2
import numpy as np

image = cv2.imread('resources/cards.jpg')

width, height = 250, 350
points = np.float32([[545, 193], [640, 80], [714, 340], [810, 225]])
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(points, point2)
imageOut = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("Cards", image)
cv2.imshow("King", imageOut)
cv2.waitKey(0)
