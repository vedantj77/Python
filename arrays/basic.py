import array as myarray

arr = myarray.array('i',[1,2,3,4,6,7,8])  # i -> integer type
arr1=myarray.array('d',[0.2,0.3,0.5,0.4]) #d -> float type
arr2=myarray.array('u',['a','c','x','m']) #u -> unicode character

#print the values of array
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print('\n')
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')
print('\n')
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print('\n')

#printing array typecodes
print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)

#printing array as it is
print(arr)
print(arr1)
print(arr2)

#printing length of array
print(len(arr))
print(len(arr1))
print(len(arr2))

#adding elements in the array
arr.insert(0,2)
arr.insert(5,1)
print(arr)

#append
arr.append(20)
print(arr)

#count - counts the occurence of a number
print(arr.count(20))
print(arr1.count(17))

#pop - removes by index 
print(arr)
arr.pop(2)
print(arr)

#remove - removes bt value
print(arr)
arr.remove(8)
print(arr)

#reversing list
lavda = [11,222,333,444,89,99]
lavda.reverse()
print(lavda.reverse)

#assigning new value
print('old array : ', arr)
arr[2]= 66
print(arr)

#reversing an array 
print(arr)
arr.reverse()
print(arr)


#fromlist
newarr1 = myarray.array('i',[])
li=[22,33,44]
newarr1.fromlist(li)
print(newarr1)
#tolist
li1=[]
li1=newarr1.tolist()
print(li1)