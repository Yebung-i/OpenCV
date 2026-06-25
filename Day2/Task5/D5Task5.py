import cv2
import numpy as np

image = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise Exception("파일 읽기 오류")

h, w = image.shape

bright = image.copy()
dark = image.copy()

for y in range(h):
    for x in range(w):
        b = int(image[y, x]) + 50
        if b > 255:
            b = 255
        bright[y, x] = b

        d = int(image[y, x]) - 50
        if d < 0:
            d = 0
        dark[y, x] = d


cv2.imshow('Original Image', image)
cv2.imshow('Bright Image', bright)
cv2.imshow('Dark Image', dark)

cv2.waitKey(0)
cv2.destroyAllWindows()
