#Resize
import cv2
imagename = '/Users/henrylin/Python/Practice/Resize and write file/photo.jpg'
img = cv2.imread(imagename, cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ',img.shape)
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0) 
cv2.destroyAllWindows()
cv2.imwrite('/Users/henrylin/Python/Practice/Resize and write file/Resized.jpg', resized)

#Write RGB as file
filename = '/Users/henrylin/Python/Practice/Resize and write file/RGB.csv'
with open (filename, 'w') as file: 
    width = int(resized.shape[1])
    height = int(resized.shape[0])
    for i in range(height): 
        for j in range(width): 
            b,g,r = (resized[i, j])
            r = str(hex(r))
            if (len(r) == 3): 
                r = r[:2] + '0' + r[2:]
            g = str(hex(g))
            if (len(g) == 3): 
                g = g[:2] + '0' + g[2:]
            b = str(hex(b))
            if (len(b) == 3): 
                b = b[:2] + '0' + b[2:]
            temp = r[2:4] + ' ' + g[2:4] + ' ' + b[2:4] + ' '
            file.write(temp)