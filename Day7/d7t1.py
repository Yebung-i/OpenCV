import numpy as np
import cv2

image = cv2.imread("lenna.bmp")
if image is None: raise Exception("영상파일 읽기 오류")

height, width = image.shape[:2]

sx, sy = 0.5, 0.5 #크기 축소해야하니 1/2로
tx = (width - (width * sx)) / 2
ty = (height - (height * sy)) / 2

M = np.array([[sx,0,tx],
              [0,sy,ty]], np.float32)

res = cv2.warpAffine(image, M, (width, height))

cv2.imshow("Image", image)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
