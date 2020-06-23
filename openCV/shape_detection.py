import numpy as np
import cv2

image = cv2.imread('resources/shapes.jpg')
imgResize = cv2.resize(image, (700, 700))
imgContour = imgResize.copy()


def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 225), 3)
            param = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * param, True)
            objCorners = len(approx)
            x, y, width, height = cv2.boundingRect(approx)
            if objCorners == 3:
                objectType = "Triangle"
            elif objCorners == 4:
                aspRatio = width/float(height)
                if 0.95 < aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCorners > 4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContour, (x, y), (x + width, y + height), (0, 225, 0), 2)
            cv2.putText(imgContour, objectType, (x + (width // 2) - 10, y + (height // 2) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContour(imgCanny)

cv2.imshow("Shapes", imgContour)
cv2.waitKey(0)
