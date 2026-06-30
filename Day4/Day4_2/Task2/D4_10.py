import os
import cv2

camera = cv2.VideoCapture(0)
if camera.isOpened() == False : raise Exception("카메라 연결 안됨")

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("width: %d" % width)
print("height: %d" % height)

fps = 30
delay = round (1000/fps)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

isRecoding = False
writer = None

while True:
    ret, frame = camera.read()
    if not ret: break
    cv2.imshow("frame", frame)

    key = cv2.waitKey(delay)

    if isRecoding and writer is not None:
        writer.write(frame)

    if key == ord('q'): break
    elif key == ord('s'):
        if not isRecoding:
            isRecoding = True
            writer = cv2.VideoWriter("temp.mp4", fourcc, fps, size)
            if writer.isOpened () == False: raise Exception("동영상 파일 개방 안됨")

    elif key == ord('e'):
        if isRecoding:
            writer.release()
            isRecoding = False

            fileName = input("파일 이름 입력")
            fullName = f"{fileName}.mp4"

            os.rename("temp.mp4", fullName)





if writer is not None:
    writer.release()
camera.release()
cv2.destroyAllWindows()
