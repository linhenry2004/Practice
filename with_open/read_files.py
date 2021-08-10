fn = '/Users/henrylin/Python/with_open/text.txt'

#read()
file_obj = open(fn)
data = file_obj.read()
file_obj.close()
print(data)

print()

#with...as keyword
with open(fn) as file_obj: 
    data = file_obj.read()
    print(data)
    file_obj.close()

print()

#Looping through the file
with open(fn) as file_obj: 
    for line in file_obj: 
        print(line)

print()

#readlines()
with open(fn) as file_obj: 
    obj_list = file_obj.readlines()
print(obj_list)

for line in obj_list: 
    print(line.rstrip()) 
#rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed). 
#If no argument is passed, it removes trailing spaces.

print()

#replace() 
with open(fn) as file_obj: 
    data = file_obj.read()
    new_data = data.replace('mango', 'banana')
    print(new_data.rstrip())

#find()
with open(fn) as file_obj: 
    obj_list = file_obj.readlines()

str = ''
for line in obj_list: 
    str += line.strip()

findstr = input('What do you need to find: ')
index = str.find(findstr)
if index >= 0:
    print(index)
else: 
    print('Index does not exist')

print()

#index() and rindex()
x = 'University of Michigan - Ann Arbor'
print(x.index('nn'))
print(x.rindex('nn'))