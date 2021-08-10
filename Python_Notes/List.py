#List: A list is a container which holds comma-separated values between square brackets. 
list = [1, 2, 3, 4, 5]
longlist = [221, -10, 94, 'no data', 3.4] #Elements does not have the same type
#2D:
Numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in longlist:
    print(i)

#List slices
'''
list[start:end]
list[:n]
list[:-n]
list[n:]
list[-n:]
list[:]
list[a:b:c] #from a to b with a step of 3
'''

#min(): find minimum
#max(): find maximum
#sum(): sum of list
#len(): length of list

#del keyword: deletes the asked element from list

'''
Add and delete elements in list:
append()
insert()
pop(): delete randomly
remove()
clear()
'''

'''
Sorting list:
reverse()
sort()
'''

'''
index()
count()
'''

'''
其他運算式：
in
not in
is
is not
'''

password = 'deepstone'
ch = input("Please enter a letter: ")
if ch in password:
    print('yes')
else:
    print('no')
if ch not in password:
    print('no')
else:
    print('yes')

x = 10
y = 10
z = 15
r = z-5
boolean_value = x is y
print(boolean_value)
boolean_value = x is z
print(boolean_value)
boolean_value = x is r
print(boolean_value)
boolean_value = x is not y
print(boolean_value)
boolean_value = x is not z
print(boolean_value)
boolean_value = x is not r
print(boolean_value)

#Sorting a list
color_list = ['Red', 'Blue', 'Green', 'Black']
print(color_list)
color_list.sort(key = None, reverse = False)
print(color_list)
color_list.reverse()
print(color_list)