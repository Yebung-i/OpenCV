import numpy as np
import cv2

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")
scale = 2
dst = np.zeros(image.shape,image.dtype)
noimage = np.zeros(image.shape, image.dtype)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        tmp = scale*int(image[i,j])
        if tmp > 255: dst[i,j] = 255
        elif tmp < 0: dst[i,j] = 0
        else: dst[i,j] = tmp

dst2 = cv2.scaleAdd(image, scale, noimage)

MinValOrigin, MaxValOrigin, MinValLocOrigin, MaxValLocOrigin = cv2.minMaxLoc(image)
MinValBright, MaxValBright, MinValLocBright, MaxValLocBright = cv2.minMaxLoc(dst)
MinValDark, MaxValDark, MinValLocDark, MaxValLocDark = cv2.minMaxLoc(dst2)

print(f"image : 최소값 = {MinValOrigin} , 최대값 = {MaxValOrigin} , 최소좌표 = ({MinValLocOrigin}) 최대좌표 =  ({MaxValLocOrigin})")
print(f"dst : 최소값 = {MinValBright} , 최대값 = {MaxValBright} , 최소좌표 = ({MinValLocBright}) 최대좌표 =  ({MaxValLocBright})")
print(f"dst2 : 최소값 = {MinValDark} , 최대값 = {MaxValDark} , 최소좌표 = ({MinValLocDark}) 최대좌표 =  ({MaxValLocDark})")

cv2.imshow("image", image)
cv2.imshow("bright", dst)
cv2.imshow("dark", dst2)
cv2.waitKey(0)
