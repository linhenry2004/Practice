def upper (func):
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print(func.__name__)
        print(args)
        return newresult
    return newFunc #Calling and running newFunc

#Setup Decorator
@upper #This means greeting(string) = upper(greeting)
def greeting(string):
    return string

print(greeting('Hello World!'))
#When we call greeting('Hello World!') here,
#we're actually calling upper(greeting('Hello World')) due to the Decorator
#Then, newFunc will take the argument 'Hello World!'
