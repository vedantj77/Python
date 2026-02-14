n = 5
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i):
        print(p,end=" ")
        p+=1
    for k in range(i+1):
        print(p,end=" ")
        p+=1
    print()

"""
p = 1

for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p +=1
    print()
"""

"""
p = 5
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p -=1
    print()
"""

"""
n = 5 
p =1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
"""

n = 5 
p =1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()