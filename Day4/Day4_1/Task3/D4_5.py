import numpy as np
import cv2

image = np.zeros((400,1200,3), np.uint8)

white = (255,255,255)

Brec = image[:, 0:400]
Grec = image[:, 400:800]
Rrec = image[:, 800:1200]

Brec[:] = (255,0,0) 
Grec[:] = (0,255,0)
Rrec[:] = (0,0,255)



cv2.rectangle(Brec, (100, 100), (300, 300), white, 10, cv2.LINE_4)
cv2.circle(Grec, (200,200), 130, white, 10)
cv2.line(Rrec, (80, 80), (320, 320), white, 10)
cv2.line(Rrec, (320, 80), (80, 320), white, 10)

cv2.imshow(' img ', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
