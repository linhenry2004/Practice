def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

def main():
    num = eval(input("Please input a number: "))
    print('The factorial of %d is' % num, factorial(num))

main()
