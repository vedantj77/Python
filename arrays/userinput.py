#taking array input from user
from array import *

arr1 = array('i',[])

n = int(input("enter length of an array : "))

for i in range(n):
    x = int(input('Enter next value: '))
    arr1.append(x)

print(arr1)

value = int(input("Enter a value: "))
print(arr1.index(value))