#Class Attribute vs. Instance Attribute
class ExampleClass(object):
    class_attr = 0
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
#instance_attr is an instance attribute defined inside the constructor
#class_attr is a class attribute defined outside the constructor

#__doc__
def getMax(x, y):
    'This is a string that will be returned by __doc__'
    if int(x) > int(y):
        return x
    else: return y

print(getMax(2, 3))
print(getMax.__doc__)

class Myclass:
    '''Myclass application'''
    def __init__ (self, x):
        self.x = x
    def printMe(self):
        '''I am in the printMe method!'''
        print('Hi', self.x)

data = Myclass(100)
data.printMe()
print(data.__doc__)
print(data.printMe.__doc__)

#__name__
print(__name__) #returns __main__
#__name__ is used to determine whether this is called by itself or imported by another file as a module

#__str__() or __repr__()
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self): #Without this line, print(a) will print the type of the object
        return '%s' % self.name

a = Name('Hung')
print(a)

#__iter__() and __next__()
class Fib():
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+ self.b
        return fib
for i in Fib(100):
    print(i)

#__getitem__()
class Subject:    
    def __add__(self, other):
        return School(self, other)

class School:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def __getitem__(self, i):
        return self.subjects[i]
Sub = School(Subject(), Subject())
print(Sub[0])

#__eq__() 邏輯方法
class City():
    def __init__(self, name):
        self.name = name
    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()

one = City('Taipei')
two = City('taipei')
print(one == two) #Calls __eq__() method

'''
更多邏輯方法
__eq__(self, other): return self == other
__ne__(self, other): return self != other
__lt__(self, other): return self < other
__gt__(self, other): return self > other
__le__(self, other): return self <= other
__ge__(self, other): return self >= other
'''

'''
更多數學方法
__add__(self, other): self + other
__sub__(self, other): self - other
__mul__(self, other): self * other
__floordiv__(self, other): self // other
__truediv__(self, other): self / other
__mod__(self, other): self % other
__pow__(self, other): self ** other
'''
