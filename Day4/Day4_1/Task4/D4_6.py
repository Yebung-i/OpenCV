
import numpy as np
import cv2
import time

image = np.zeros((300,300), np.uint8)

count = 0
isCounting = False
LastTime = time.time()


while True:
    image.fill(255)

    if isCounting:
        curTime = time.time()

        if curTime - LastTime >= 1.0:
            count += 1
            LastTime = curTime

    cv2.putText(image, str(count), (110, 190), cv2.FONT_HERSHEY_SIMPLEX, 4, 0, 5)
    cv2.imshow(' TimeCount ', image)

    key = cv2.waitKey(10)

    if key == ord('s'):
        if not isCounting:
            LastTime = time.time()
            isCounting = True

    elif key == ord('t'):
        isCounting = False

    elif key == ord('r'):
        isCounting = False
        count = 0

    elif key == ord ('q'):
        break;

cv2.destroyAllWindows()
