'''
Modes: 
'r': read mode (preset)
'w': write mode
'a': append mode
'x': new file mode
'b': binary mode
't': text mode (preset)
'''

#File processing in python
with open("/Users/henrylin/Python/with_open/text.txt") as myfile:
    #if today file is stored somewhere else, you will need to specify the location
    #Ex: files/notes.txt if it is under a folder "files"
    content = myfile.read()
    myfile.seek(0) #Cursor returns to the top of the file
    print(content)

#Create new .txt file and write on it
with open("/Users/henrylin/Python/with_open/newtext.txt", "w") as newfile:
    newfile.write("This is a new note\nYay I'm on the next line")

#Append new things onto a created file
with open("/Users/henrylin/Python/with_open/text.txt", "a") as myfile:
    myfile.write("\nbanana")
