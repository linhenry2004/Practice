import numpy as np
import cv2

filename = 'images/photo.jpg'
kernel = np.ones((5, 5), np.uint8)

img = cv2.imread(filename)
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imGray, (11, 11), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=3)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('Gray Image', imGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Gray Blur Image', imgBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Canny Image', imgCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Dilation Image', imgDilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
