#fibonacci series starts with 0 1 and then every number starting from its 3rd index is the sum of previous 2 numbers
n=int(input("Enter a number : "))
a=0
b=1

if n<=0:
    print('enter a positive number greater thane 0 !')
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
        
