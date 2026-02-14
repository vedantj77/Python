#Print elements of an array in reverse order.
from array import*

#using in-built functions
arr1=[11,22,33,44,55,66,77]
arr1.reverse()
print(arr1)

#using slice operation
#sequence of slice [start:stop:step]
""" Why is Slicing Used in Python?
Extracting subarrays or substrings
Reversing sequences ([::-1])
Skipping elements ([::2] for every second element)
Making copies of lists ([:]) """


print('reverse : ', arr1[::-1])