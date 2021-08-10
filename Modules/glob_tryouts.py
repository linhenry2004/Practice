import glob

print('Method 1: Print all files: ')
for file in glob.glob('/Users/henrylin/Python'): 
    print(file)

print('Method 2: Print all currently working files: ')
for file in glob.glob('/Users/henrylin/Python/Python_Notes/Class*.py'): 
    print(file)

print('Method 3: List all currently working files: ')
for file in glob.glob('/Users/henrylin/Python/Python_Notes/Call*.*'): 
    print(file)