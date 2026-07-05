import numpy as np
import cv2

image = cv2.imread("lenna.bmp")
if image is None: raise Exception("영상파일 읽기 오류")

height, width = image.shape[:2]
doubleW = width * 2
doubleH = height * 2

center = (width / 2, height / 2)
angle = -45
scale = 2.0

M = cv2.getRotationMatrix2D(center, angle, scale)

M[0, 2] += (doubleW / 2) - (width / 2)
M[1, 2] += (doubleH / 2) - (height / 2)

res = cv2.warpAffine(image, M, (doubleW, doubleH))

cv2.imshow("Image", image)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
