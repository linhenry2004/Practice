import cv2
import numpy as np

filename = 'images/cards.jpg'
img = cv2.imread(filename)

width, height = 810, 1350
pts1 = np.float32([[957, 144], [1338, 290], [669, 618], [1109, 814]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image", imgOutput)

cv2.waitKey(0)
cv2.displayOverlay()
