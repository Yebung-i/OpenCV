import numpy as np, cv2

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

kernel = np.ones((7,7), np.float32)/ 49
kernel2 = np.array([[-1,-1,-1],
                    [-1,9,-1],
                    [-1,-1,-1]], dtype=np.float32)

blur = cv2.filter2D(image,-1,kernel)

cv2.imshow("blur", blur)

sharp = cv2.filter2D(blur, -1, kernel2)

cv2.imshow("sharp", sharp)
cv2.waitKey(0)
