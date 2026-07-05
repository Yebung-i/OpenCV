import numpy as np
import cv2

image = cv2.imread("lenna.bmp")
if image is None: raise Exception("영상파일 읽기 오류")

height, width = image.shape[:2]
center = (width / 2, height / 2)

totalAngle = 0

cv2.imshow("image", image)
cv2.imshow("res", image)

while True:
    key = cv2.waitKey(0)
    
    if key == ord('r'):
        totalAngle -= 10
    elif key == ord('b'):
        totalAngle += 10
    elif key == ord('q'):
        break
    else:
        continue
    
    M = cv2.getRotationMatrix2D(center, totalAngle, 1.0)
    res = cv2.warpAffine(image, M, (width, height))
    
    cv2.imshow("res", res)
    
cv2.destroyAllWindows()
