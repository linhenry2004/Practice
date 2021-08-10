#Args: The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
'''
- The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
- What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. 
- With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
- For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
- Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
'''

#Basic function with *args
def basic (*args): 
    for arg in args: 
        print(arg)

basic('Hello', 'my', 'name', 'is', 'Henry')

#Function with an extra argument
def extra (argument, *args):
    print('Extra argument:', argument)
    for arg in args: 
        print('*args arguments:', arg)

extra('Hello', 'my', 'name', 'is', 'Henry')

#**kwargs: The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
#          We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
'''
- A keyword argument is where you provide a name to the variable as you pass it into the function.
- One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
- That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
'''

#Basic function with **kwargs
def basic2 (**kwargs): 
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))

basic2(first = 'Hello', second = 'my', third = 'name', fourth = 'is', fifth = 'Henry')

#Function with an extra argument
def extra2 (argument, **kwargs):
    print('Extra argument:', argument)
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))

extra2('Hi', first = 'Hello', second = 'my', third = 'name', fourth = 'is', fifth = 'Henry')

#*args and **kwargs combined in a function
def combined (*args, **kwargs): 
    print("args:", args)
    print("kwargs:", kwargs)

combined('Hello', 'my', 'name', 'is', 'Henry', first = 'Hello', second = 'my', third = 'name', fourth = 'is', fifth = 'Henry')

#Using *args and **kwargs to call a function
def called (arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

args = ('Hello', 'World', '!')
called(*args)

kwargs = {'arg1': 'Hello', 'arg2': 'World', 'arg3': '!'}
called(**kwargs)

# *args and **kwargs for classes: 
class Person: 
    '''person entity'''

    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.age = age
    
    def __repr__(self):
        return f'Person(first_name={self.first_name}, surname={self.surname}, age={self.age})'
    
    def __lt__(self, other):
        return self.age < other.age

data = [
    {'first_name':"John", 'surname':'Smith', 'age':13},
    {'first_name':"Anne", 'surname':'McNell', 'age':11},
    {'first_name':'Mary', 'surname': 'Brown', 'age':14}
]

results = [Person(**row) for row in data] #inputs rows in data one-by-one in a **kwargs manner
print(results)