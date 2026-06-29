import numpy as np
import cv2

image = np.zeros((300, 300), np.uint8)
black = 0
count = 0

for i in range(count, 9):
    cv2.putText(image, count, (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 4, black)
    cv2.imshow(' img ', image)
    cv2.waitKey(1000)
cv2.destroyAllWindows()

