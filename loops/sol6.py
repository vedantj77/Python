#find factorial of a number using for loop
n = int(input('Enter the factorial number : '))
fact = 1
while n > 0:
    fact=fact*n
    n-=1
print('Factorial of the number is :',fact)