import time

#time()
print(int(time.time()))
#Returns the number of seconds that has passed since 1970/1/1 00:00:00 AM

#sleep(seconds): Stops the current work
fruits = ['apple', 'banana', 'watermelon', 'peach', 'mango']
for fruit in fruits:
    print(fruit)
    time.sleep(0.1)

#asctime()
print(time.asctime())

#localtime()
xtime = time.localtime()
print(xtime)
for i in xtime:
    print(i)
