import csv
import cv2
from PIL import Image
import numpy as np

barray = []
filename = '/Users/henrylin/Python/Practice/Resize and write file/RGB.csv'
with open (filename, 'r') as file: 
    pixels = file.readline()
    barray = bytearray.fromhex(pixels)
    a = np.frombuffer(barray, dtype = np.uint8)

z = np.reshape(a, newshape = (750, 500, 3))
for row in range (300, 400):
    for col in range(200, 300):
        for i in range(3): 
            s = z[row][col][i] + 100
            z[row][col][i] = s if s < 255 else 255
new_image = Image.fromarray(z)
new_image.save('/Users/henrylin/Python/Practice/Resize and write file/From_csv2.jpg')