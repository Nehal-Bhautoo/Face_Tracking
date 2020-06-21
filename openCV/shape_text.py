import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

# color image
# image[:] = 255, 0, 0

# add line to image
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (0, 255, 0), 3)

# add rectangle to image
cv2.rectangle(image, (0, 0), (250, 350), (0, 0, 255), 2)

# add circle to image
cv2.circle(image, (400, 50), 30, (255, 255, 0), 5)

# add text
cv2.putText(image, " Open_CV ", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)


cv2.imshow("Image", image)
cv2.waitKey(0)
