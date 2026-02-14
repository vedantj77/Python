#defining a function in python

def func(x,y):
    print('Rum',x,y)
    return x*y

#func(5,6) #this will call the function
print(func(5,6)) #this will also print the return statement


def bocha(to="locha"):     
    print("Hello, " +to)

bocha() 
name = input("suggest a name ?")
bocha(name)  #name = to


def eod(num):
    if num%2==0:
        print('even')
    else:
        print('odd')

x=int(input("Enter number to see even/odd"))
eod(x)




