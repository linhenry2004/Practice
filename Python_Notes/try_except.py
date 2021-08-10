#try-except:
#try:
#    operations
#except someError:
#    operations
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('You cannot divide by 0!')

print(division(10, 2))
print(division(5, 0))

#try-except-else:
#try:
#    operations
#except someError:
#    operations
#else: Do this when try works properly
#    operations
fn = 'ch15_4.txt'
try:
    with open(fn) as file_Obj:
        data = file_Obj.read()
except FileNotFoundError:
    print("File not found")
else: #Done if try works well
    print(data)

#Exception keyword: 通用錯誤
print('\n')
#finally keyword: operated when leaving the algorithm
def Division(x, y):
    try:
        return x/y
    except Exception as e:
        print(e)
    finally:
        print('Finished')

print(Division(10, 2), '\n')
print(Division(5, 0), '\n')
print(Division('a', 'b'), '\n')
print(Division(6, 3), '\n')
