import numpy as np
import cv2

image = cv2.imread("scaling.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

height, width = image.shape[:2]
center = (width / 2, height / 2)

scale = 1.5
resHeight = int(height * scale)
resWidth = int(width * scale)

res = np.zeros((resHeight, resWidth), dtype = np.uint8)

for y in range(height):
    for x  in range(width):
        xd = int(x*scale)
        yd = int(y*scale)
        
        if 0 <= xd < resWidth and 0 <= yd < resHeight:
            res[yd, xd] = image[y, x]

cv2.imshow("image", image)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
