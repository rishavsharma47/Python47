import cv2, time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("==check==")
print(check)

print("==frame==")
print(frame)

time.sleep(5)

print("Releasing Video")
video.release()

cv2.imshow("MyFrame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


