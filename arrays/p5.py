#Calculate sum and product of array elements.

arr1=[11,22,33,44,55,66,77,88]
sum=0
product=1

for i in arr1:
    sum += i
    product *=i

print('sum :', sum)
print("product of all elements :", product)