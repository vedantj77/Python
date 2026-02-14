#Count occurrences of a target number in an array.

arr = [11,22,33,44,55,66,77,88,99,11,22,33,11,22,33]
target=int(input())
count = 0 

for i in arr:
    if target == i:
        count +=1

print(count)
