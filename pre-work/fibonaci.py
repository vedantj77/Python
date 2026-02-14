#fibonacci series using functions

x= int(input('Enter a number : '))

a=0
b=1

def fibo(n):
    global a,b
    if n <= 0:
        print()
    elif n ==1:
        print(0)
    elif n==2:
        print(0)
        print(1)
    else:
        print(a)
        print(b)
    
    for i in range(2,n):
        c = a + b
        print(c)
        a=b
        b=c

fibo(x)

#fibonacci series without functions 

n = int(input("Enter a number : "))

a=0
b=1
if n<0:
    print("Enter a positive number! ")
elif n<=0:
    print('Please enter a value greater than 0')
elif n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)

for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c


#fibonacci series using recursion

def fibo(n):
    if n < 2:
        return n
    else:
        return(fibo(n-2)+fibo(n-1))
    

x=int(input('Enter number of terms : '))
n=x
for i in range(0,n+1):
    print(fibo(i))


