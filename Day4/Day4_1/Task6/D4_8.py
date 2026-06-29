import numpy as np
import cv2

center = (250, 250)

black = 0
currentPos = [250,250] #현위치 (처음은 중앙)
step = 50  # 방향키를 누를 때마다 이동할 픽셀 크기
thick = 2

image = np.zeros((500,500,3),np.uint8)
image[:] = (255,255,255)


while True:
    cv2.imshow(' img ', image)

    key = cv2.waitKeyEx(50)
    if key == ord('q') : break
    elif key == 0x250000:
        prevPos = list(currentPos)
        currentPos[0] -= step
        cv2.line(image, tuple(prevPos), tuple(currentPos), black, thick)
    elif key == 0x260000:
        prevPos = tuple(currentPos)
        currentPos[1] -= step
        cv2.line(image, tuple(prevPos), tuple(currentPos), black, thick)
    elif key == 0x270000:
        prevPos = tuple(currentPos)
        currentPos[0] += step
        cv2.line(image, tuple(prevPos), tuple(currentPos), black, thick)
    elif key == 0x280000:
        prevPos = tuple(currentPos)
        currentPos[1] += step
        cv2.line(image, tuple(prevPos), tuple(currentPos), black, thick)
        
cv2.destroyAllWindows()
