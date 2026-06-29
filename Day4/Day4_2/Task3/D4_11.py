
import cv2

capture = cv2.VideoCapture("stopwatch.avi")
if not capture.isOpened(): raise Exception("파일읽기 오류")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))
print("width: %d" % width)
print("height: %d" % height)
print("fps: %d" % fps)

delay = round(1000/ fps)
size = (width, height) 
fourcc = cv2.VideoWriter_fourcc(*'XVID')

writer = cv2.VideoWriter("output.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    output = cv2.add(frame, 100)
    writer.write(output)
    cv2.imshow('frame', frame)
    cv2.imshow('bright', output)
    if cv2.waitKey(delay) >= 0: break

capture.release()
writer.release()
