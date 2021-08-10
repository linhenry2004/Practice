import cv2

filename = 'images/photo.jpg'
img = cv2.imread(filename)
cv2.imshow("Test", img)
cv2.waitKey()
cv2.destroyAllWindows()
