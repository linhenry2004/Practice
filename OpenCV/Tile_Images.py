import cv2

image1 = 'images/RGB.jpg'
image2 = 'images/RGB_gray.jpg'
image3 = 'images/BGR.jpg'
image4 = 'images/Red.jpg'
image5 = 'images/Green.jpg'
image6 = 'images/Blue.jpg'
image7 = 'images/Red_Visualize_Channel.jpg'
image8 = 'images/Green_Visualize_Channel.jpg'
image9 = 'images/Blue_Visualize_Channel.jpg'

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
cv2.imwrite(
    'images/Tiled.jpg', img_final)
