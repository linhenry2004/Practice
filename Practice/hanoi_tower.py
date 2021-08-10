def main ():
    n = eval(input("Please enter a number: "))
    cmove(n, 'a', 'b', 'c')

def cmove (n, a, b, c):
    if n == 1:
        print("Move 1 from tower %s to %s" % (a,c))
    else:
        cmove(n-1, a, c, b)
        print("Move %d from tower %s to %s" % (n, a, c))
        cmove(n-1, b, a, c)

main()
