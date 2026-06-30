
import cv2
import numpy as np

image = np.zeros((500, 500, 3), np.uint8)
image.fill(255)
title = "img"
bar_name = "Color"

isClicked = False
prevLocation = (0,0)

colorDic = {
    "blue" : (255,0,0),
    "green" : (0,255,0),
    "red" : (0,0,255)
}

def PASS(x):
    pass

def getColor():

    pos = cv2.getTrackbarPos(bar_name, title) # 트랙바 이름, 이미지 이름으로 해당하는 트랙바의 값을 찾아옴

    if pos == 0:
        return colorDic["blue"]
    elif pos == 1:
        return colorDic["green"]
    elif pos == 2:
        return colorDic["red"]


def clickMouse(event, x, y, flage, param):
    global isClicked, prevLocation

    if event == cv2.EVENT_LBUTTONDOWN:
        if not isClicked:
            prevLocation = (x,y)
            isClicked = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if isClicked:
            color = getColor()
            cv2.line(image, prevLocation, (x,y), getColor(), 2)
            cv2.imshow(title, image)
            prevLocation = (x,y)


    elif event == cv2.EVENT_LBUTTONUP:
        if isClicked:
            isClicked = False

cv2.imshow(title, image)
cv2.setMouseCallback(title, clickMouse)
cv2.createTrackbar("Color", title, 0,2, PASS)

while True:
    if cv2.waitKey(1) >= 0 : break

cv2.destroyAllWindows()
