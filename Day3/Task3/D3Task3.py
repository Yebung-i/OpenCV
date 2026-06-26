import cv2
import numpy as np

img = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
if img is None:
    raise Exception("파일 읽기 오류")

def onMouse(event, x, y, flage, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"좌표: ({x},{y}), 화소값(B,G,R): {img[y,x]}")

cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
