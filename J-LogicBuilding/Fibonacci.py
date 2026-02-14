#fibonacci series starts with 0 1 and then every number starting from its 3rd index is the sum of previous 2 numbers

n = int(input('Enter Fibonacci Series Length :'))

a=0
b=1

if n == 0:
    print(0)
elif n == 1:
    print(a)
    print(b)
else :
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)        