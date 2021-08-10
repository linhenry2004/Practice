src = 'bdata'
bytedata = bytes(range(0, 256))

with open(src, 'wb') as file:
    file.write(bytedata)

with open(src, 'rb') as file: 
    print(file.tell())
    file.seek(10)
    print(file.tell())
    data = file.read()
    print(data[0])
    file.seek(255)
    print(file.tell())
    data = file.read()
    print(data[0])