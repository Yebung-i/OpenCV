import numpy as np
import cv2

def calcGrayHist(image):
    images = [image]
    channels = [0]
    hsize = [256] 
    ranges = [0, 256]
    hist = cv2.calcHist(images, channels, None, hsize, ranges)
    return hist

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("파일 읽기 오류")

total_pixels = image.shape[0] * image.shape[1]
min_val, max_val, _, _ = cv2.minMaxLoc(image)

hist = calcGrayHist(image)

# argmax => 배열에서 가장 큰 값이 있는 인덱스를 찾는 함수
most_freq_pixel = np.argmax(hist)     
most_freq_count = int(hist[most_freq_pixel].item())
pixel_80_count = int(hist[80].item())

print(f"영상의 전체 픽셀수:{total_pixels}")
print(f"영상에서 픽셀값의 최소값:{int(min_val)}")
print(f"영상에서 픽셀값의 최대값:{int(max_val)}")
print(f"빈도수가 가장많은 픽셀값과 빈도수:{most_freq_pixel},{most_freq_count}")
print(f"픽셀값 80의 빈도수 :{pixel_80_count}")

cv2.imshow("src", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
