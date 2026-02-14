#Print alternate elements of an array.

#using slicing
arr1 = [11,22,33,44,55,66,77,88,99,100]
print(arr1[::2])

#using for loop
for i in range(0,len(arr1),2):
    print(arr1[i],end=' ')
