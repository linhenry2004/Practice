#__getitem__(): Returns the acquired value
class fib(): 
    def __init__(self,start=0,step=1):
        self.step=step
    def __getitem__(self, key): 
            a = key+self.step
            return a

s=fib(0, 5)
print(s[1])

#__setitem__(): Allows one to set value so it can be returned by __getite__()
class Fib():
    def __init__ (self):
        self.changed = {}
    def __getitem__(self, key):
        return self.changed[key]
    def __setitem__(self, key, value):
        self.changed[key] = value

s = Fib()
s[1] = 4 #__setitem__()
print(s[1]) #__getitem__()