print('Hello World!') #Normal print()
str1 = 'Hello'
str2 = 'World!'
print(str1, str2) #print() with comma
print(str1 + ' ' + str2) #print() with + sign

'''
%d: 格式化整數輸出
%f: 格式化浮點數輸出
%x: 格式化16進位整數輸出
%X: 格式化大寫16正數輸出
%o: 格式化8進位整數輸出
%s: 格式化字串輸出
%e: 格式化科學記號e的輸出
%E: 格式化科學記號大寫E的輸出
'''

print('%s %s' % (str1, str2))
print('%d' % 15)
print('%e' % 15)
print('%f' % 15)
print('%o' % 15)
print('%x' % 15)

'''
%(+|-)nd: 格式化整數輸出
%(+|-)m.nf: 格式化浮點數輸出
%(+|-)nx: 格式化16進位整數輸出
%(+|-)no: 格式化8進位整數輸出
%(+|-)ns: 格式化字串輸出
%(+|-)m.ns: m是輸出字串寬度，n是顯示字串長度，n可以剪裁字串
%(+|-)e: 格式化科學記號e的輸出
%(+|-)E: 格式化科學記號大寫E的輸出
'''

print("%f" % 5.1234567890)
print("%.5f" % 5.1234567890)
print("%9.5f" % 5.1234567890)
print("%015.5f" % 5.1234567890)
print("% 9f" % 5.1234567890)
print("% 9f" % -5.1234567890)
print("%+9f" % 5.1234567890)
print("% 9f" % -5.1234567890)
print("%-9.4f" % 5.1234567890)

#.format():
score = 90
name = "James"
count = 1
print("{}, your score for your {}st exam is {}".format(name, count, score))
