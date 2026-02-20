#remove duplicates from string

name = input('Enter a string : ')
new_name=""

for i in range(len(name)):
    if name[i] not in new_name:
        new_name += name[i]

print(new_name)













#remove duplicates from unsorted list

mylist = [1,2,3,1,2,3,4,5]
new_list=[]

for i in mylist:
    if i not in new_list:
        new_list.append(i)

print(new_list)
