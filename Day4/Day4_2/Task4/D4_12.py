import cv2

capture = cv2.VideoCapture("stopwatch.avi")
count = 0
fps = 30

total = 377

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

size = (width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter("output.mp4", fourcc, fps, size)

while True:
    ret, frame = capture.read()
    if not ret : break

    cv2.imwrite(f"Frame{count:04d}.jpg", frame)
    count += 1

for i in range(total-1, -1, -1):
    fileName = f"Frame{i:04d}.jpg"
    frameIn = cv2.imread(fileName)

    if frameIn is None:
        print(f"{fileName} 파일 못찾음")
        continue

    writer.write(frameIn)


writer.release()
