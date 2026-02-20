def CalSum(a,b):
    sum=a+b
    print(sum)

CalSum(22,11)
CalSum(1,44)
CalSum(22,99)


#defining a function in python
print('LETS LEARN ABOUT RETURN STATEMENT')
def func(x,y):
    print('Rum',x,y)
    return x*y

func(5,6) #this will call the function
print(func(5,6)) #this will also print the return statement


print('LETS LEARN ABOUT PARAMETERS AND ARGUMENTS')

def cal_prod(j=1,k=2): #these parameters j=1 and k=2 are default values and will be printed if the function is called without any arguments
    print(j+k)

cal_prod() # the function is called without passsing any arguments
cal_prod(5,6)


#USING FUNCTIONS

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *=i
    print(f)

fact(5)
fact(6)
fact(7)


print('USER INPUT IN FUNCTIONS')

def eod(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
        
x = int(input('Enter a number : '))
eod(x)