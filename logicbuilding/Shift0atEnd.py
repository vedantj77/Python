mylist = [0,1,2,3,0,4,5,0,3]

for i in range(len(mylist)):
    if mylist[i] == 0:
        mylist.append(0)
        del mylist[i]


print(mylist)