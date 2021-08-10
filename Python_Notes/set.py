langs = {'Python', 'C++', 'Java'}

#Characteristics of set
langs = {'Python', 'C++', 'Java', 'C++', 'Java'}
print(langs)

#set()
x = set('DeepStone mean Deep Learning')
print(x)

fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits)
print(x)

cities = set(('Beijing', 'Tokyo', 'Beijing', 'Taipei', 'Tokyo'))
print(cities)

'''
Set operations:
&: intersection
|: union
-: difference
^: symmetric difference
==: equals
!=: not equals
<=: issubset
>=: issuperset
in: is in
not in: is not in
'''

'''
Set methods:
add(): 加一個元素到集合
clear(): 刪除集合所以元素
copy(): 複製集合
difference_update(): 刪除集合與另一集合重複的元素
discard(): 如果是集合成員則刪除
intersection_update(): 可以使用集合更新集合內容
isdisjoint(): 如果兩個集合沒有交集返回True
issubset(): 如果另一個集合包含這個集合返回True
isupperset(): 如果這個集合包含另一個集合返回True
pop(): 傳回所刪除的元素，如果是空集合返回False
remove(): 刪除指定元素，如果此元素不存在，城市將返回KeyError
symmetric_differende_update(): 使用對稱差集更新集合內容
update(): 使用聯集更新集合內容
enumerate()
len()
max()
min()
sorted()
sum()
'''

#frozenset: sets that can't be changed
x = frozenset([1, 3, 5])
print(x)
