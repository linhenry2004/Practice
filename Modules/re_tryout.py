import re

#compile()
phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')

'''
正則表達式的特殊字元
\d: 0-9之間的整數字元
\D: 除了0-9之間的整數字元以外的其他字元
\s: 空白、定位、Tab鍵、換行、換頁字元
\S: 除了空白、定位、Tab鍵、換行、換頁字元以外的其他字元
\w: 數字、字母和底線_字元，[A-Za-z0-9_]
\W: 除了數字、字母和底線_字元，[A-Za-z0-9_]，以外的其他字元
'''

#search()
def parseString_search(string):
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.search(string)
    if phoneNum != None:
        print('The number is %s' % phoneNum.group())
    else:
        print('\'%s\' does not contain a phone number' % string)

#findall()
def parseString_findall(string):
    phoneRule = re.compile(r'(\d{4})-(\d{3})-(\d{3})')
    phoneNum = phoneRule.findall(string)
    print('The number is %s' % phoneNum)

string1 = 'My phone number is 0930-919-919'
string2 = 'Hello World!'
parseString_search(string1)
parseString_search(string2)

print()

parseString_findall(string1)
parseString_findall(string2)

print()

#groups()
message = 'My phone number is 02-28352835'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, message)
areaNum, localNum = phoneNum.groups()
print('Area number:', areaNum)
print('Local number:', localNum)

print()

'''
Special Characters:
.: In the default mode, this matches any character except a newline. 
   If the DOTALL flag has been specified, this matches any character including a newline. 
^: Matches the beginning of the string or line. 
   For example /^A/ does not match the 'A' in "about Articles" but does match it in "Articles of life"
$: Matches the end of the string or line. 
   For example, /e$/ does not match the 't' in "exact", ut does match it in "w3resource".
*: Matches the previous character 0 or more times. 
   For example, /bo*/ matches 'boo' in "A bootable usb" and 'b' in "A beautiful mind", but nothing in "A going concern".
+: Matches the previous character 1 or more times. 
   For example, /a+/ matches the 'a' in "Daniel" and all the a's in "Daaam"
?: Matches the previous character 1 or more times. 
   For example, /r?eu?/ matches the 're' in "w3resource" and the 'eu' in "europe"
{m}: Specifies that exactly m copies of the previous RE should be matches; fewer matches cause the entire RE not to match.
     For example, b{5} will match exactly five 'b' characters but not four.
{m,n}: Causes the resulting RE to match from m to n repititions of the preceding RE. 
\: Either escapes special characters or signals a special sequence; special sequences are discussed below. 
[]: Used to indicate a set of characters
|: A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. 
'''

mon = re.search(r'(\d{4})-(\d{2})-(\d{2})', '2018-09-01')
print(mon.groups())
print(mon.group())
print(mon.group(1))
print(mon.group(2))
print(mon.group(3))

print()

#Nesting Groups
mon = re.search(r'(((\d{4})-\d{2})-\d{2})', '2018-09-01')
print(mon.groups())
print(mon.group())
print(mon.group(1))
print(mon.group(2))
print(mon.group(3))

print()

#re.findall() match string: 
source = 'split all string' 
print(re.findall('[\w]+', source))

print()

#|: 
message = 'John and Tom will attend the party. John is short'
pattern = 'Mary|John|Tom'
txt = re.findall(pattern, message) #find all that fits
print(txt)

print()

#?: 
message = 'Johnson will attend the party'
pattern = 'John((na)?son)'
txt = re.search(pattern, message)
print(txt.group())

message = 'Johnnason will attend the party'
pattern = 'John((na)?son)'
txt = re.search(pattern, message)
print(txt.group())

print()

#*: 
message = 'Johnson will attend the party'
pattern = 'John((na)*son)'
txt = re.search(pattern, message)
print(txt.group())

message = 'Johnnason will attend the party'
pattern = 'John((na)*son)'
txt = re.search(pattern, message)
print(txt.group())

message = 'Johnnananananason will attend the party'
pattern = 'John((na)*son)'
txt = re.search(pattern, message)
print(txt.group())

print()

#+: 
message = 'Johnson will attend the party'
pattern = 'John((na)+son)'
txt = re.search(pattern, message)
print(txt)

message = 'Johnnason will attend the party'
pattern = 'John((na)+son)'
txt = re.search(pattern, message)
print(txt.group())

message = 'Johnnananananason will attend the party'
pattern = 'John((na)+son)'
txt = re.search(pattern, message)
print(txt.group())

print()

#[^]: 
message = 'John, Johnson, Johnnason and Johnnathan will attend the party'
pattern = '[^aeiouAEIOU]' #Find all that does not include
txt = re.findall(pattern, message)
print(txt)

print()

#^: 
message1 = 'John will attend the party'
message2 = 'His name is John'
pattern = '^John' #Checks if she is in front
print(re.findall(pattern, message1))
print(re.findall(pattern, message2))

print()

#$: 
message1 = 'John will attend the party.'
message2 = 'I am 28'
print(re.findall('\W$', message1))
print(re.findall('\d$', message1))
print(re.findall('\W$', message2))
print(re.findall('\d$', message2))

print()

#.: 
message = 'Cat hat sat at matter flat'
pattern = '.at'
txt = re.findall(pattern, message)
print(txt)

print()

#.*: 
message = 'Name: Henry Lin Address: Somewhere why should you know'
pattern = 'Name: (.*) Address: (.*)'
txt = re.findall(pattern, message)
print(txt)

print()

#Name Grouping
pattern = '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
mon = re.search(pattern, '2018-09-01')
print(mon.group('year'))
print(mon.group('month'))
print(mon.group('day'))

print()

#re.match() method
message = 'John will attend my party tonight.'
pattern = 'John'
txt = re.match(pattern, message)
if txt != None: 
   print(txt.group())
else: 
   print('Test failed')

message = 'My best friend is John.'
txt = re.match(pattern, message, re.DOTALL)
if txt != None: 
   print(txt.group())
else: 
   print('Test failed')

print() 

'''
MatchObject methods: 
group(): 可傳回搜尋到的字串
end(): 可傳回搜尋到字串的結束位置
start(): 可傳回搜尋到字串的起始位置
span(): 可傳回搜尋到字串的（起始，結束）位置
'''

#result = re.sub(pattern, newstr, message)
message = 'Eli Nan will attend the party. My best friend is Eli Nan.'
pattern = 'Eli Nan'
newstr = 'Kevin Thomson'
txt = re.sub(pattern, newstr, message)
if txt != message:
   print('Successful:', txt)
else: 
   print('Failed:', txt)

pattern = 'Eli Thomson'
txt = re.sub(pattern, newstr, message)
if txt != message: 
   print('Successful:', txt)
else: 
   print('Failed:', txt)

print()

#Multiline Pattern
message = '''02-88223349, (02)-26669999, 02-29998888 ext 123, 
             12345678, 02 33887766 rxt. 12222'''
pattern = r'''(
   (\d{2}|\(\d{2}\))?
   (\s|-)?
   \d{8}
   (\s*(ext|ext.)\s*\d{2,4})?
   )'''
phoneNum = re.findall(pattern, message, re.VERBOSE)
print(phoneNum)

print()

'''
re.IGNORECASE/re.DOTALL/re.VERBOSE
Can be used in re.search(), re.finall(), re.match(), or re.compile()
However, you can only use one of which in the parameters
re.IGNORECASE: Ignores upper case/lower case
re.DOTALL: Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline. 
re.VERBOSE: This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. 
'''