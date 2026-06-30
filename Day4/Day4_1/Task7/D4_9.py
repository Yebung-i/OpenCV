
import cv2
import numpy as np

image = np.zeros((500, 500, 3), np.uint8)
image.fill(255)
title = "img"
bar_name = "Color"

isClicked = False
prevLocation = (0,0)

def getColor():
    if color == 0:
        return (255,0,0)
    elif color ==


def clickMouse(event, x, y, flage, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if not isClicked:
            prevLocation = (x,y)
            isClicked = True
        elif event == cv2.EVENT_LBUTTONUP:
            if isClicked:
                cv2.line(image, prevLocation, (x,y), getColor(), 2)

cv2.imshow(title, image)
cv2.createTrackbar("Color", title, 0,2)
cv2.setMouseCallback(title, clickMouse)

while True:
    if cv2.waitKey(1) : break

cv2.destroyAllWindows()
