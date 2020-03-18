import cv2
import numpy as np

video = cv2.VideoCapture(0)

frameCount = 0
while True:

    check, frame = video.read()
    frameCount += 1
    print(frame)
    cv2.imshow("MyVideo", frame)
    # cv2.imshow("MyVideo", rot90(frame))

    key = cv2.waitKey(1) # 1 is 1 milli se

    if key == ord("q"):
        break

print(">> Total Frames Captuerd:", frameCount)
video.release()
cv2.destroyAllWindows()