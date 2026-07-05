import numpy as np
import cv2

image = cv2.imread("lenna.bmp")
if image is None: raise Exception("영상파일 읽기 오류")

height, width = image.shape[:2]
center = (width / 2, height / 2)

totalAngle = 0

cv2.imshow("image", image)
cv2.imshow("res", image)
cv2.waitKey(1)

while True:


    inputKey = input("회전각도를 입력하시오 : ")
    
    if inputKey == 'q':
        break
    else:
        angle = float(inputKey)
        
    totalAngle += angle
    
    M = cv2.getRotationMatrix2D(center, totalAngle, 1.0)
    res = cv2.warpAffine(image, M, (width, height))
    
    cv2.imshow("image", image)
    cv2.imshow("res", res)
    cv2.waitKey(1)

cv2.destroyAllWindows()
