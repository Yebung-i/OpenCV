import numpy as np
import cv2

image = np.zeros((400, 400), np.uint8)
image[:] = 255
black = 0

pt1, pt2 = (100, 100), (300, 300)
pt3, pt4 = (300, 100), (100, 300)
center = (image.shape[1]//2, image.shape[0]//2)

cv2.rectangle(image, pt1, pt2, black , 1, cv2.LINE_4)

cv2.circle(image, center, 100, black)

cv2.imshow('Line & Circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
