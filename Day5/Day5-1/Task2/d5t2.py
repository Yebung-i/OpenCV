import numpy as np
import cv2

def onChange(value):
    global image, title

    res = cv2.add(image, value)
    cv2.imshow(title, res)

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("파일 읽기 오류")

title = "image"

cv2.imshow(title, image)
cv2.createTrackbar("Brightness", title, 0, 255, onChange)
cv2.waitKey(0)
