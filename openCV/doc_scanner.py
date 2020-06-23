import cv2
import numpy as np

frameWidth = 480
frameHeight = 640

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


def processing(image):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray, (5, 5), 1)
    imageCanny = cv2.Canny(imageBlur, 200, 200)
    kernel = np.ones((5, 5))
    imageDial = cv2.dilate(imageCanny, kernel, iterations=2)
    imageErode = cv2.erode(imageDial, kernel, iterations=1)
    return imageErode


def getContour(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    biggest = np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            param = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * param, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, biggest, -1, (0, 0, 225), 20)
    return biggest


def order(points):
    points = points.reshape((4, 2))
    pointsNew = np.zeros((4, 1, 2), np.int32)
    add = points.sum(1)
    pointsNew[0] = points[np.argmin(add)]
    pointsNew[3] = points[np.argmax(add)]
    difference = np.diff(points, axis=1)
    pointsNew[1] = points[np.argmin(difference)]
    pointsNew[2] = points[np.argmax(difference)]
    return pointsNew


def getWarp(image, big):
    big = order(big)
    point1 = np.float32(big)
    point2 = np.float32([[0, 0], [frameWidth, 0], [0, frameHeight], [frameWidth, frameHeight]])
    matrix = cv2.getPerspectiveTransform(point1, point2)
    imageOutput = cv2.warpPerspective(image, matrix, (frameWidth, frameHeight))
    return imageOutput


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgContour = img.copy()
    imageResult = processing(img)
    biggest = getContour(imageResult)
    print(biggest)
    if biggest.size != 0:
        imageWrap = getWarp(img, biggest)
        cv2.imshow("Result", imageWrap)
    else:
        cv2.imshow("Image Result", imageResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
