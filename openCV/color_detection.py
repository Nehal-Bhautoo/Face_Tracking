import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 320)
cv2.createTrackbar("Hue Min", "TrackBars", 82, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 160, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 9, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 220, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 25, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 170, 255, empty)


while True:
    image = cv2.imread('resources/car.jpg')
    imgResize = cv2.resize(image, (1200, 800))
    imageHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imageHSV, lower, upper)

    imageResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)

    cv2.imshow("Car", imageResult)
    cv2.waitKey(1)
