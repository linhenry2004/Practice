src = '/Users/henrylin/Python/with_open/MUSIC.jpg'
dst = '/Users/henrylin/Python/with_open/MUSIC1.jpg'
tmp = ''

with open(src, 'rb') as file: 
    tmp = file.read()
    with open(dst, 'wb') as file_wr: 
        file_wr(tmp)