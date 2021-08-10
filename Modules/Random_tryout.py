import random

#randint(): Random integer
n = 3
for i in range(n):
    print(random.randint(1, 100))

#choice(): Choose randomly from a list
fruits = ['apple', 'banana', 'watermelon', 'peach', 'mango']
print(random.choice(fruits))

#shuffle():
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for i in range(n):
    random.shuffle(poker)
    print(poker)

#sample():
lotteries = random.sample(range(1, 50), 7)
specialNum = lotteries.pop()
for lottery in sorted(lotteries):
    print(lottery, end = ' ')
print()

#uniform(): Random floating point
for i in range(n):
    print(random.uniform(1, 10), end = ' ')
print()

#random(): uniform method that returns x such that 0 <= x < 1
for i in range(n):
    print(random.random(), end = ' ')
print()
