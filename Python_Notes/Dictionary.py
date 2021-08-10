#Dictionary consists of a key and a value
name_dict = {'key':'value', 'key2':'value2', 'key3':'value3', 'key4':'value4', 'key5':'value5'}
print(name_dict)

#add keys to Dictionary
name_dict['key6'] = 'value6'
print(name_dict)

#Change
name_dict['key'] = 'value1'
print(name_dict)

#Delete
del name_dict['key']
print(name_dict)

#items():
for key, value in name_dict.items():
    print(key, 'corresponds to', value)

#pop()
name_dict.pop('key2')
print(name_dict)

#popitem(): randomly pops on element
name_dict.popitem()
print(name_dict)

#clear(): clears whole Dictionary
name_dict.clear()
print(name_dict)

#Delete whole dictionary
del name_dict

#Create empty Dictionary
fruits = {}
fruits = {'watermelon':15, 'banana':20, 'peach':25}
print(fruits)

#copy()
cfruits = fruits.copy()
print(cfruits)

#update()
more_fruits = {'apple':18, 'orange':13}
fruits.update(more_fruits)
print(fruits)

#dict(): turns 2D-lists into dictionary
nation = [['Japan', 'Tokyo'], ['Taiwan', 'Taipei'], ['England', 'London']]
nationDict = dict(nation)
print(nationDict)

#Dictionary in a Dictionary
account = {'cshung':{
                     'last_name':'Hong',
                     'first_name':'Kong',
                     'city':'Taipei'},
           'kevin':{
                     'last_name':'Zheng',
                     'first_name':'asdfjh',
                     'city':'Beijing'}}

#Dictionary Methods:
#len()
print(len(account))
print(len(account['cshung']))
print(len(account['kevin']))
#fromkeys()
seq1 = ['name', 'city']
print(dict.fromkeys(seq1))
print(dict.fromkeys(seq1, 'Chicago'))

seq2 = ('name', 'city')
print(dict.fromkeys(seq2))
print(dict.fromkeys(seq2, 'New York'))

#get()
fruits = {'watermelon':15, 'banana':20, 'peach':25}
print(fruits.get('banana'))

#setdefault()
print(fruits.setdefault('orange',100))
#Instead of just printing 100, it also adds the 'orange' key into the fruits dictionary
print(fruits)
