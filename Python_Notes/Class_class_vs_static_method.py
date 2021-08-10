#classmethod first item in parameter is cls instead of self
#Can be called by the class instead of the object
class Counter():
    counter = 0
    def __init__(self):
        Counter.counter += 1
    
    @classmethod
    def show_counter(cls):
        print('class method')
        print('counter =', cls.counter)
        print('counter =', Counter.counter) #cls makes it easu to access the class

one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()

#staticmethod is a classmethod without the cls argument
class Pizza():
    @staticmethod
    def demo():
        print('I like pizza') #Used only when the method does not need to access the class

Pizza.demo()