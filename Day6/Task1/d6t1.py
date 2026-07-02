import numpy as np
import cv2
import time

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)

forNoise = np.random.randint(-30, 31, size=image.shape, dtype=np.int32)

noiseImage = image.astype(np.int32) + forNoise
noiseImage = np.clip(noiseImage,0,255).astype(np.uint8)

kernel3 = np.ones((7,7), np.float32) / 49
blur = cv2.filter2D(image, -1, kernel3)

cv2.imshow("src", image)
cv2.imshow("Noise", noiseImage)
cv2.imshow("blur3", blur)
cv2.waitKey(0)
