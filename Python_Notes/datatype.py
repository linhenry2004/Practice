#type(): returns the type of the variable
a = 10
b = a/3
print(type(a))
print(type(b))

#bin(): returns the binary number
c = 0b1101
print(c)
d = 13
print(bin(d))

#oct(): returns octagonal number
e = 0o57
print(e)
f = 47
print(oct(f))

#hex(): returns hexadecimal number
g = 0x5D
print(g)
h = 93
print(hex(h))

#int(): turns variable into integer
#float(): turns variable into a floating point
i = 10.5
j = 6
print(i)
print(int(i))
print(j)
print(float(j))

#abs(): absolute value
#pow(x,y): x to the y power
#round(): Bankers Rounding
#         Odd number: 四捨五入
#         Even number: 五捨六入
#Complex number
print(complex(3,5))
x = 6 + 9j
print(x.real())
print(x.imag())

'''
String Special Characters
\': " ' "
\": " " "
\\: " \ "
\a: 響鈴
\b: Backspace
\f: Change Page
\n: Change line
\o: Octagonal number
\r: Mouse move to the most left
\x: Hexadecimal number
\t: Tab
\v: Vertical
'''

#str(): Turn variable into a string

#open(): For examples, look at with_open 
file_obj = open('file.txt', mode="r")
#mode types:
'''
'r': read mode (preset)
'w': write mode
'a': append mode
'x': new file mode
'b': binary mode
't': text mode (preset)
'''

#input()
name = input("Please input a name: ")
print("Your name is", name)

#eval()
number = eval(input("Please input a number: ")) #Evaluates the input
