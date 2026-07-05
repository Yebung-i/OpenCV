import numpy as np
import cv2

def calcGrayHist(image):
    images = [image]
    channels = [0]
    hsize = [256] 
    ranges = [0, 256]
    hist = cv2.calcHist(images, channels, None, hsize, ranges)
    return hist

def drawGrayHistImage(hist):
    win_shape = (100, 256)
    hist_img = np.full(win_shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, win_shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0] 
    for i, h in enumerate(hist.flatten()):
        x = int(round(i * gap)) 
        w = int(round(gap))
        cv2.line(hist_img, (x, 0), (x, int(h)), 0, 1)
    return cv2.flip(hist_img, 0)

image = cv2.imread("crayfish.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

min_val, max_val, _, _ = cv2.minMaxLoc(image)
dst = ((image - min_val) / (max_val - min_val) * 255.0).astype(np.uint8)

hist1 = calcGrayHist(image)
hist_image1 = drawGrayHistImage(hist1)

hist2 = calcGrayHist(dst)
hist_image2 = drawGrayHistImage(hist2)

cv2.imshow("src", image)
cv2.imshow("dst", dst)
cv2.imshow("srcHist", hist_image1)
cv2.imshow("dstHist", hist_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
