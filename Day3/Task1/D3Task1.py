import cv2
import numpy as np

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

down = 0
up = 0
move = 0

def mouse(event, x, y, flags ,parm):
    global down, up, move

    if event == cv2.EVENT_LBUTTONDOWN:
        down += 1
        print("EVENT_LBUTTONDOWN : ", down)
    
    elif event == cv2.EVENT_LBUTTONUP:
        up += 1
        print("EVENT_LBUTTONUP : ", up)

    elif event == cv2.EVENT_MOUSEMOVE:
        move += 1
        print("EVENT_MOUSEMOVE : ", move)

cv2.imshow("img", img)
cv2.setMouseCallback("img", mouse)

while True:
    if cv2.waitKey(0) == 27: break

cv2.destroyAllWindows()
