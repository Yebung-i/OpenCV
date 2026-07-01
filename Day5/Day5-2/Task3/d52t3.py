import numpy as np
import cv2
import time

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: 
    raise Exception("파일 읽기 오류")

dst = np.zeros(image.shape, image.dtype)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        x = int(image[i,j])

        if 0 <= x <= 128:
            tmp = (78/128) * (x-128) + 128
        elif 128 < x <= 200:
            tmp = (127/72) * (x - 128) + 128
        else:
            tmp = 255

        if tmp > 255:
            dst[i,j] = 255
        elif tmp < 0:
            dst[i,j] = 0
        else:
            dst[i,j] = int(round(tmp)) #반올림

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
