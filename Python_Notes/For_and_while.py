#while loop
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
i = 0
while i < len(Numbers):
    total += Numbers[i]
    i+= 1
print('total = ', total)

#for loop
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in Numbers:
    print(i)

#Looping keywords
#break: exit loop immediately
#continue: exit current loop and go to the next loop
#pass: do nothing and exit

#for...else loop:
num = int(input("Please input a number greater than 1: "))
if num == 2:
    print("%d is prime" % num)
else:
    for n in range(2, num):
        if num % n == 0:
            print("%d is not prime" % num)
            break #If the loop did not break here, it will run the else statement
    else:
            print("%d is prime" % num)

#while...else loop:
x = 0
s = 0
while (x < 10):
     s = s + x
     x = x + 1
else: #executed when while loop's condition is no longer true
     print('The sum of first 9 integers : ',s) 
#while...else can also be terminated by break

#range()
for x in range(3):
    print(x)

#Enumerate method
drinks = ['coffee', 'tea', 'wine']
for value, name in enumerate(drinks):
    print(value, name)
