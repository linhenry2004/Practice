import numpy as np
import cv2
from matplotlib import pyplot as plt

#read/write picture and then display
imagename = '/Users/henrylin/Python/Practice/Picture Practice/RGB.jpg'
img = cv2.imread(imagename)
img_gray = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imshow('My Image', img)
cv2.imshow('My Grayscale Image', img_gray)
cv2.waitKey()
cv2.destroyWindow('My Grayscale Image')
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/RGB_gray.jpg', img_gray)
cv2.waitKey()
cv2.destroyWindow('My Image')
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/RGB_PNG.png', img)

#OpenCV reads the file as BGR, so without turning it into RGB, matplotlib will misread the info
img_bgr = cv2.imread(imagename)
plt.imshow(img_bgr)
plt.show()

img_bgr = cv2.imread(imagename)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/BGR.jpg', img_rgb) #Misread file
plt.imshow(img_rgb)
plt.show()

img_gray = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray, cmap = 'gray')
plt.show()

#Split
image = cv2.imread(imagename)
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.moveWindow('Red', 0, -70)
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Red.jpg', R)
cv2.imshow("Green", G)
cv2.moveWindow('Green', 600, -70)
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Green.jpg', G)
cv2.imshow("Blue", B)
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Blue.jpg', B)
cv2.moveWindow('Blue', 0, 370)
cv2.waitKey()
cv2.destroyAllWindows()

#Merge
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyWindow('Merged')
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Merged.jpg', merged)

#Visualize each channel in “color” rather than “grayscale”
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Red_Visualize_Channel.jpg', cv2.merge([zeros, zeros, R]))
cv2.waitKey()
cv2.destroyWindow('Red')

cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Green_Visualize_Channel.jpg', cv2.merge([zeros, G, zeros]))
cv2.waitKey()
cv2.destroyWindow('Green')

cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Blue_Visualize_Channel.jpg', cv2.merge([B, zeros, zeros]))
cv2.waitKey()
cv2.destroyWindow('Blue')

#Tile 9 pictures together into 3 by 3
image1 = '/Users/henrylin/Python/Practice/Picture Practice/RGB.jpg'
image2 = '/Users/henrylin/Python/Practice/Picture Practice/RGB_gray.jpg'
image3 = '/Users/henrylin/Python/Practice/Picture Practice/BGR.jpg'
image4 = '/Users/henrylin/Python/Practice/Picture Practice/Red.jpg'
image5 = '/Users/henrylin/Python/Practice/Picture Practice/Green.jpg'
image6 = '/Users/henrylin/Python/Practice/Picture Practice/Blue.jpg'
image7 = '/Users/henrylin/Python/Practice/Picture Practice/Red_Visualize_Channel.jpg'
image8 = '/Users/henrylin/Python/Practice/Picture Practice/Green_Visualize_Channel.jpg'
image9 = '/Users/henrylin/Python/Practice/Picture Practice/Blue_Visualize_Channel.jpg'

img1 = cv2.imread(image1)
img2 = cv2.imread(image2)
img3 = cv2.imread(image3)
img4 = cv2.imread(image4)
img5 = cv2.imread(image5)
img6 = cv2.imread(image6)
img7 = cv2.imread(image7)
img8 = cv2.imread(image8)
img9 = cv2.imread(image9)

im_v1 = cv2.vconcat([img1, img4, img7])
im_v2 = cv2.vconcat([img2, img5, img8])
im_v3 = cv2.vconcat([img3, img6, img9])
img_final = cv2.hconcat([im_v1, im_v2, im_v3])
cv2.imshow('Tiling Test', img_final) 
cv2.waitKey(0)
cv2.destroyWindow('Tiling Test')
cv2.imwrite('/Users/henrylin/Python/Practice/Picture Practice/Tiled.jpg', img_final)