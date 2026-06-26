import numpy as np
import cv2

color = [
    (255,0,0),
    (0,255,0),
    (0,0,255)
]
image = np.zeros((200, 400, 3), np.uint8)
i = 0
while True:
    image[:,:] = color[i%3]
    i = i + 1
    cv2.imshow('win', image)
    if cv2.waitKey(1000) == 27: break
