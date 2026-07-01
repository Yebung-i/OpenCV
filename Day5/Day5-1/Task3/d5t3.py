import numpy as np
import cv2

def onChange(value):
    global image, title, isAdd

    if value == 0:
        if isAdd == True:
            isAdd = False
    
    else:
        if isAdd == False:
            isAdd = True

def onMouse(event, x, y, flage, param):
    global image, title, isAdd

    if event == cv2.EVENT_LBUTTONDOWN:
        if isAdd == True:
            image = cv2.add(image, 10)
            cv2.imshow(title, image)
        else:
            image = cv2.subtract(image, 10)
            cv2.imshow(title, image)    


    

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("파일 읽기 오류")

isAdd = False
title = "image"

cv2.imshow(title, image)
cv2.createTrackbar("Brightness", title, 0, 1, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
