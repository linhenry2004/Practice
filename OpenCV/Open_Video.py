import cv2

filename = 'images/OpenCV test.mp4'
cap = cv2.VideoCapture(filename)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cv2.destroyAllWindows()
