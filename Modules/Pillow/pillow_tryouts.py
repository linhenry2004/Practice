from PIL import ImageColor as IC
from PIL import Image
from PIL import ImageDraw as ID
from PIL import ImageFont as IF

#getrgb() method
print(IC.getrgb('#0000ff'))
print(IC.getrgb('rgb(0, 0, 255)'))
print(IC.getrgb('rgb(0%, 0%, 100%)'))
print(IC.getrgb('Blue'))
print(IC.getrgb('blue'))

print()

#getcolor() method
print(IC.getcolor('#0000ff', 'RGB'))
print(IC.getcolor('rgb(0, 0, 255)', 'RGB'))
print(IC.getcolor('Blue', 'RGB'))
print(IC.getcolor('#0000ff', 'RGBA'))
print(IC.getcolor('rgb(0, 0, 255)', 'RGBA'))
print(IC.getcolor('Blue', 'RGBA'))

print()

#Box Tuple
#(left, top, right, bottom) -> Box Tuple
#left = 左上角x座標
#top = 左上角y座標
#right = 右下角x座標
#bottom = 右下角y座標

'''
Basic operations
open() method: open() a jpg file
size() method: get width and height of file
'''

#Basic operations
filename = '/Users/henrylin/Python/Modules/Pillow/MUSIC.jpg'

rushMore = Image.open(filename)
print(type(rushMore))
width, height = rushMore.size
print(width)
print(height)
print(rushMore.filename)
print(rushMore.format)
print(rushMore.format_description)
rushMore.save(filename)
rushMore.show()

pict = Image.new('RGB', (300, 180), 'aqua')
pict.save('/Users/henrylin/Python/Modules/Pillow/aqua.jpg')

print()

#resize() method
pict = Image.open(filename)
width, height = pict.size
newPict1 = pict.resize((width*2, height))
newPict1.save('/Users/henrylin/Python/Modules/Pillow/MUSIC2.jpg')
newPict2 = pict.resize((width, height*2))
newPict2.save('/Users/henrylin/Python/Modules/Pillow/MUSIC3.jpg')

#rotate() method
pict.rotate(90).save('/Users/henrylin/Python/Modules/Pillow/MUSIC4.jpg')
pict.rotate(180).save('/Users/henrylin/Python/Modules/Pillow/MUSIC5.jpg')
pict.rotate(270).save('/Users/henrylin/Python/Modules/Pillow/MUSIC6.jpg')

#transpose() method
pict.transpose(Image.FLIP_LEFT_RIGHT).save('/Users/henrylin/Python/Modules/Pillow/MUSIC7.jpg')
pict.transpose(Image.FLIP_TOP_BOTTOM).save('/Users/henrylin/Python/Modules/Pillow/MUSIC8.jpg')

#getpixel() method
pict = Image.open(filename)
print(pict.getpixel((150, 50)))

#putpixel() method
newImage = Image.new('RGBA', (300, 300), 'Yellow')
for x in range(50, 251): 
    for y in range(50, 151): 
        newImage.putpixel((x, y), (0, 255, 255, 255))
for x in range(50, 251): 
    for y in range(151, 251): 
        newImage.putpixel((x, y), IC.getcolor('Blue', 'RGBA'))
newImage.save('/Users/henrylin/Python/Modules/Pillow/putpixel.png')

print() 

#crop() method
pict = Image.open(filename)
cropPict = pict.crop((80, 30, 150, 100))
cropPict.save('/Users/henrylin/Python/Modules/Pillow/MUSIC10.jpg')

#copy() method
copyPict = pict.copy()
copyPict.save('/Users/henrylin/Python/Modules/Pillow/MUSIC11.jpg')

#paste() method
pict = Image.open(filename)
copyPict = pict.copy()
cropPict = copyPict.crop((80, 30, 150, 100))
copyPict.paste(cropPict, (20, 20))
copyPict.paste(cropPict, (20, 100))
copyPict.save('/Users/henrylin/Python/Modules/Pillow/MUSIC11.jpg')

'''
Filters: 
BLUR: 模糊
CONTOUR: 輪廓
DETAIL: 細節增強
EDGE_ENHANCE: 邊緣增強
EDGE_ENHANCE_MORE: 深度邊緣增強
EMBOSS: 浮雕效果
FIND_EDGES: 平滑效果
SMOOTH: 邊緣訊息
SMOOTH_MORE: 平滑效果
SHARPEN: 銳利化效果
'''

'''
ImageDraw Module: 
point([(x1, y1), ... (xn, yn)], fill)
line([x1, y1], ... (xn, yn)], width, fill)
ellipse((left, top, right, bottom), fill, outline)
rectangle((left, top, right, bottom), fill, outline)
polygon([(x1, y1), ... (xn, yn)], fill, outline)
'''
newImage = Image.new('RGBA', (300, 300), 'Yellow')
drawObj = ID.Draw(newImage)

for x in range(100, 200, 3): 
    for y in range(100, 200, 3):
        drawObj.point([x,y], fill='Green')
drawObj.line([(0,0), (299,0), (299,299), (0,299), (0,0)], fill='Black')
for x in range(150, 300, 10):
    drawObj.line([(x,0), (300,x-150)], fill='BLue')
for y in range(150, 300, 10):
    drawObj.line([(0,y), (y-150, 300)], fill='Blue')

drawObj.rectangle((0, 0, 299, 299), outline='Black')
drawObj.ellipse((30, 60, 130, 100), outline='Black')
drawObj.ellipse((65, 65, 95, 95), fill='Blue')
drawObj.ellipse((170, 60, 270, 100), outline='Black')
drawObj.ellipse((205, 65, 235, 95), fill='Blue')
drawObj.polygon([(150, 120), (180, 180), (120, 180), (150, 120)], fill='Aqua')
drawObj.rectangle((100, 210, 200, 240), fill='Red')
newImage.save('/Users/henrylin/Python/Modules/Pillow/ImageDraw.png')

#Text in Image
newImage = Image.new('RGBA', (600, 300), 'Yellow')
drawObj = ID.Draw(newImage)

strText = 'University of Michigan'
drawObj.text((50, 50), strText, fill='Blue')
fontInfo = IF.truetype('/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)

strCtext = 'Ann Arbor'
fontInfo = IF.truetype('/System/Library/Fonts/Supplemental/SourceCodePro-Light.ttf')
drawObj.text((50, 180), strCtext, fill='Blue', font=fontInfo)
newImage.save('/Users/henrylin/Python/Modules/Pillow/textImage.png')