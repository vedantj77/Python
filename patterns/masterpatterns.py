#Increasing Triangle 

n = 5 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#Decreasing Triangle 
print("/n")
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()


#Right Sided Triangle 

print("/n")
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")

    print()


#Right Sided Downwards Triangle 
print("/n")
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i,n):
        print("*",end=" ")
    
    print()

#Hill pattern 
print("/n")
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()

#  Reverse Hill pattern 
print('/n')
for i in range(n):
    for i in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for k in range(i,n-1):
        print("*",end=" ")
    print()