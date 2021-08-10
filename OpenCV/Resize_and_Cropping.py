import cv2

filename = 'images/photo.jpg'
img = cv2.imread(filename)

print(img.shape)

imgResize = cv2.resize(img, (200, 175))
imgCropped = img[0:200, 200:500]

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
