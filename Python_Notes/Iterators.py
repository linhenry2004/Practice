my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print()

my_iterable = [4, 7, 0, 3]
iter_obj = iter(my_iterable)
while True: 
    try: 
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
print()

#Custom iterators
class PowTwo: 
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else: 
            raise StopIteration
numbers = PowTwo(3)
i = iter(numbers)
while True:
    try: 
        element = next(i)
        print(element)
    except StopIteration:
        break
print()