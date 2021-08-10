#Tuple is a list that no elements can be changed
numbers = (1, 2, 3, 4, 5)

#zip(): Zips multiple elements
fields = ['Name', 'Age', 'Hometowm']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)
print(type(zipData))
player = list(zipData)
print(player)

#generator
number = (n for n in range(6))
for num in number:
    print(num)

#tuple()
tuplefstr = tuple('Hello World')
print(tuplefstr)