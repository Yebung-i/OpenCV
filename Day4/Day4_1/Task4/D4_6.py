import numpy as np
import cv2


black = 0
blue = (255,0,0)

count = 5
h = 500
w = 500

Hor = h // count
Ver = w // count

curX = count // 2
curY = count // 2

while True:
    image = np.zeros((h, w, 3), np.uint8)
    image[:] = (255,255,255)

    Xstart = curX * Ver
    Ystart = curY * Hor
    Xend = Xstart + Ver
    Yend = Ystart + Hor

    cv2.rectangle(image, (Xstart, Ystart), (Xend,Yend), blue, cv2.FILLED)

    for i in range(0, count):
        y = i * Hor
        cv2.line(image, (0,y),(w,y), black, 1, cv2.LINE_4)

    for i in range(0, count):
        x = i * Ver
        cv2.line(image, (x,0), (x,h), black, 1, cv2.LINE_4)

    cv2.imshow(' Line ', image)



    key = cv2.waitKeyEx(50)
    if key == 27 : break
    elif key == 0x250000:
        if curX > 0: curX -= 1
    elif key == 0x260000:
        if curY > 0: curY -= 1
    elif key == 0x270000:
        if curX < count -1 : curX += 1 
    elif key == 0x280000:
        if curY < count -1 : curY += 1

cv2.destroyAllWindows()
