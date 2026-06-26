import numpy as np
import cv2

def onMouse(event, x, y, flage, param):
    global r,g,b,img
    
    if event == cv2.EVENT_RBUTTONDOWN:
        r = 0
        g = 0
        if(b == 0):
            b = 255

    elif event == cv2.EVENT_LBUTTONDOWN:
        b = 0
        g = 0
        if(r == 0):
            r = 255

    img[:] = (b,g,r)
    cv2.imshow(title, img)

r = 255
g = 255
b = 255

img = np.zeros((300, 500, 3), np.uint8)
title = "src"
cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
