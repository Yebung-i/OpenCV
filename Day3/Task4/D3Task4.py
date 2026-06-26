import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
if src is None:
    raise Exception("파일 읽기 오류")

def onChange(value):
    global count
    count += 1
    print("트랙바 이벤트 횟수: ", count)
    print("트랙바 위치: ", value)

title = 'src'
count = 0
location = 0

cv2.imshow('src', src)

cv2.createTrackbar("level", title, 1, 16, onChange)
cv2.waitKey(0)
cv2.destroyWindow(title)
