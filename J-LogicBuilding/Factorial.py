n = int(input("Enter a number to calculate its factorial: "))
a = 1

for i in range(1,n+1):
    a *= i 

print(a)


#USING FUNCTIONS

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *=i
    print(f)

fact(5)
fact(6)
fact(7)


#Using Recurrsion

def fact(n):
    if n==0 or n==1:
        return 1
    return  n * fact(n-1)

print(fact(5))


