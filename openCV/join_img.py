import cv2
import numpy as np

image = cv2.imread('resources/user.jpg')
image2 = cv2.resize(image, (250, 250))

h_img = np.hstack((image2, image2))
# v_img = np.vstack((image, image))

cv2.imshow('Horizontal', h_img)
# cv2.imshow('Vertical', v_img)
cv2.waitKey(0)
