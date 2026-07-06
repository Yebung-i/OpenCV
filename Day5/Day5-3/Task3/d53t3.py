import numpy as np
import cv2

def mycalcGrayHist(image):
    hist = np.zeros((256, 1), dtype=np.float32)
    height, width = image.shape[:2]
    for y in range(height):
        for x in range(width):
            pixel_value = image[y, x]
            hist[pixel_value][0] += 1
    return hist

def mydrawGrayHistImage(hist):
    win_shape = (100, 256)
    hist_img = np.full(win_shape, 255, np.uint8) 
    
    cv2.normalize(hist, hist, 0, win_shape[0], cv2.NORM_MINMAX)
    h_data = hist.flatten()
    
    for i in range(255): 
        pt1 = (i, int(h_data[i]))
        pt2 = (i + 1, int(h_data[i + 1]))

        cv2.line(hist_img, pt1, pt2, 0, 1)

    return cv2.flip(hist_img, 0)

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

hist = mycalcGrayHist(image)
hist_image = mydrawGrayHistImage(hist)

cv2.imshow("src", image)
cv2.imshow("srcHist", hist_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
