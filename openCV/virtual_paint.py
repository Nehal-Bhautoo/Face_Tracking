import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [[5, 107, 0, 16, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]

colorValue = [[0, 253, 58],
              [0, 255, 0],
              [255, 0, 255]]

point = []


def findColor(image, colors, values):
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    count = 0
    new_point = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imageHSV, lower, upper)
        x, y = getContour(mask)
        cv2.circle(imgResult, (x, y), 10, values[0], cv2.FILLED)
        if x != 0 and y != 0:
            new_point.append([x, y, count])
        count += 1
    return new_point


def getContour(image):
    x, width, y = 0, 0, 0
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            param = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * param, True)
            x, y, width, height = cv2.boundingRect(approx)
    return x + width // 2, y


def drawImage(points, value):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, value[2], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    new_point = findColor(img, myColors, colorValue)
    if len(new_point) != 0:
        for new_points in new_point:
            point.append(new_points)
    if len(point) != 0:
        drawImage(point, colorValue)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
