import binascii

a = b'This is a byte'
print(a)

#decode(): 
b = b'\x45\x6c\x20\x6e\x69\xc3\xb1\x6f\x20\x63\x6f\x6d\x65\x20\x63\x61\x6d\x61\x72\xc3\xb3\x6e'
print(b)
print(b.decode())

#fromhex(): 
c = '45678c6c56f205876f72c6'
print(c)
d = bytes.fromhex(c)
print(d)

#ord(): 
print(ord(b'm')) #Returns the ASCII Decimal number

#Turn bytes to list
print(list(b'Python bytes'))

#Convert bytes to hex
print(binascii.hexlify("Python".encode("utf8")))

#chr(): 
print(chr(60)) #Returns the character that equals the ASCII decimal number

#bytearray: 
e = bytearray(b'Python Bytes')
print(e)

#Difference between string and bytearray
del e[11:15]
print(e)

e.append(45)
print(e)