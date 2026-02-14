#tuples in python are immuteable i.e cant be changed once declared

tup = (12,21,34,55,'Vedant')
print(tup)


#sets are not in sequence and doesnt maintain duplicate values
set = {12,212,29,'Vedant',12}
print(set)
print(4 in set) #checks if it is in the set or not


t=(1,2,3,44,3,2,)
b=t.index(2) # Find the index of the first occurrence of the value `2` in the tuple
print(b)