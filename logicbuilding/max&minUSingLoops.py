mylist = [1,2,3,5,9,11,40]

max = min = mylist[0]

for i in mylist:
    if max < i :
        max = i

    if min > i :
        min = i


print('Max : ',max)
print('Min :',min)
