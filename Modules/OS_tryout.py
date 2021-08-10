import os

#os.getcwd(): Get current working directory
print(os.getcwd())

#os.path.abspath(): Get absolute path
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('assert.py'))

#os.path.relpath(): Get relative path
print(os.path.relpath('/Users/henrylin'))
print(os.path.relpath('/Users/henrylin/Python'))
print(os.path.relpath('/Users/henrylin', 'assert.py'))

#exist(path): If path exists, return True, else return False
#isabs(path): If path is an absolute path, return True, else return False
#isdir(path): If path is a folder(directory), return True, else return False
#isfile(path): If path is a file, return True, else return False

print(os.path.exists('/Users/henrylin/Python'))
print(os.path.exists('asdfjkhasdfgljkd;nfvn'))

print(os.path.isabs('/Users/henrylin/Python/Python_Practice/assert.py'))
print(os.path.isabs('asdfhkasdf'))

print(os.path.isdir('/Users/henrylin/Python'))
print(os.path.isdir('/Users/henrylin/asdlkjasdf'))

print(os.path.isfile('/Users/henrylin/Python/Python_Practice/assert.py'))
print(os.path.isfile('/Users/henrylin/Python'))

#mkdir(path): Make a path directory
#rmdir(path): Remove path directory
#remove(path): remove path file
#chdir(path): change current directory to path
#join(): Join all arguments in parameters into a directory

files = ['args_kwargs.py', 'assert.py', 'Dictionary.py']
for file in files: 
    print(os.path.join('/Users/henrylin/Python/Python_Practice', file))

#os.path.getsize(): Get the size of a file
print(os.path.getsize('/Users/henrylin/Python/Python_Practice/Dictionary.py'))

#os.listdir(): Print everything inside the directory
print(os.listdir('/Users/henrylin/Python/Python_Practice'))

#os.walk(): 
'''
The 3 returned values by os.walk(): 
dirName: Directory name
sub_dirNames: All the directory names under the given directory
fileNames: All the file's names under the working directory
'''
print('----------------------------------------------------------------------------------')
for dirName, sub_dirNames, fileNames in os.walk('/Users/henrylin/Python/Python_Practice'): 
    print(dirName)
    print(sub_dirNames)
    print(fileNames, '\n')