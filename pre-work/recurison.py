#1 to 10 in python

def printN(n):
    if n == 0:
        return
    else:
        printN(n-1)
        print(n)

printN(10)


#print 10 to 1 in python using recursion

def rec(n):
    if n == 0:
        return
    print(n)
    rec(n-1)


rec(10)

