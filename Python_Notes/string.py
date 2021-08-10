from datetime import datetime

s = 'Python String'
print(s)
print(s[4])
print(s[-4])
print(s[0:6])
print(s[:8])
print(s[4:])

'''
String Methods:
lower(): make lowercase
upper(): make uppercase
title(): capitalize first letter
swapcase(): Swap cases
rstrip(): Delete excess spaces in the end
lstrip(): Delete excess spaces at the front
strip(): Delete excess spaces at both ends
center(): Make words in the center
rjust(): Make words to the right
ljust(): Make words to the left
zfill()
'''

'''
String Boolean Checks:
isuppper()
islower()
isdigit()
isalpha()
'''

# + operator: 
a = 'Python' + 'String'
print(a)

# += operator: 
a = 'Java'
b = 'Script'
a+=b
print(a)

# * operator
c = '<' + a*3 + '>'
print(c)

#len()
print(len(c))

#Search method example: 
def search(char,str):
    L=len(str)
    print(L)
    i = 0
    while i < L:
        if str[i]== char:
            return 1
            i = i + 1
        return -1

print(search("P","PYTHON"))

#String Formatting
print('{} {}'.format('Python', 'Format'))
print('{1} {0}'.format('Python', 'Format'))

class Data(object):
    def __str__(self):
        return 'Python'
    def __repr__(self):
        return 'Format'

print('{0!s} {0!r}'.format(Data()))

#More types of formatting
print('{:>15}'.format('Python'))
print('{:15}'.format('Python'))
print('{:<{}s}'.format('Python', 15))
print('{:15}'.format('Python'))
print('{:*<15}'.format('Python'))
print('{:^16}'.format('Python'))
print('{:.10}'.format('Python Tutorial'))
print('{:.{}}'.format('Python Tutorial', 10))
print('{:d}'.format(24))
print('{:f}'.format(5.12345678123))
print('{:5d}'.format(24))
print('{:05.2f}'.format(5.12345678123))
print('{:+d}'.format(24))
print('{:-d}'.format((-24)))
print('{: d}'.format(24))
print('{:=6d}'.format((- 24)))
data = {'first': 'Place', 'last': 'Holder!'}
print('{first} {last}'.format(**data))
print('{first} {last}'.format(first='Place', last='Holder!'))
print('{:%Y-%m-%d %H:%M}'.format(datetime(2016, 7, 26, 3, 57))) #datetime imported