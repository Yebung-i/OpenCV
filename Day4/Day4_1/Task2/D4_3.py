import numpy as np
import cv2

image = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
white = (255,255)


count = 3
h = image.shape[0]
w = image.shape[1]

Hor = h // count
Ver = w // count

for i in range(1, count):
    y = i * Hor
    cv2.line(image, (0,y),(w,y), white, 1, cv2.LINE_4)

for i in range(1, count):
    x = i * Ver
    cv2.line(image, (x,0), (x,h), white, 1, cv2.LINE_4)

cv2.imshow(' Line ', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
