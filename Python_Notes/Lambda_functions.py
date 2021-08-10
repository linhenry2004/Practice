#original function
def square(x):
    return x ** 2
print(square(10))

#lambda function
#Basic setup: lambda arguments: expression
square = lambda x: x ** 2
print(square(10))

#Advanced lambda function:
second_lambda = lambda a: 'green' if a < 10 else 'orange' if 10 <= a < 20 else 'red'
#reads the value of a, green if a is less than 10, orange if a is between 10 and 20, or red otherwise
print(second_lambda(15)) #prints orange

#function inside function:
def mycar(cars, func):
    for car in cars:
        print(func(car))
def wdcar(carbrand):
    return "My dream car is " + carbrand.title()
dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, wdcar)

#filter()
#filter(func, iterable)
#iterable includes anything that can return its members one at a time
#iterables include strings, tuples, lists, etc
mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(lambda x: (x % 2 == 1), mylist)
#lambda function: puts item into filter_object iff x is an odd number
print([item for item in filter_object])
longlist = [123, 12.3, -145, 'True', 'Hello']
new_longlist = [i if isinstance(i, int) else 0 for i in longlist]
#if i is not an instance of integer, it will append 0 into new_longlist.
#Otherwise, it will append the original vaulue
print(new_longlist)

#map(function, iterable)
mylist = [5, 10, 15, 20, 25, 30]
squarelist = list(map(lambda x: x**2, mylist))
print(squarelist)
