fn = '/Users/henrylin/Python/with_open/newtext.txt'
string = 'Hello World!'

with open(fn, 'w') as file: 
    file.write(string + '\n')
    file.write(str(100) + '\n')

with open('/Users/henrylin/Python/with_open/newnewtext.txt', 'a') as file: 
    file.write(string + '\n')
    file.write(str(100) + '\n')

zenofPython = '''Beautiful is better than ugly. 
Explicit is better than implicits. 
Simple is better than complex. 
Flat is better than nested. 
Sparse si better than desse. 
Readability counts. 
Special cases aren't special enough to break the rules. 
...
...
By Tim Peters'''
size = len(zenofPython)
offset = 0
chunk = 100
with open(fn, 'w') as file: 
    while True: 
        if offset > size:
            break
        print(file.write(zenofPython[offset:offset+chunk]))
        offset += chunk