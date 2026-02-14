#upside hill
n = 5
print("This is Upside Hill")
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    for k in range(i):
        print('*',end='')
    print()

#pascal triangle using *
print("This is Pascal triangle")
n = 10
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()


##
print("This is increasing triangle ")
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()

##
print("This is Decreasing Triangle ")
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end="")
    print()


#this is downside hill
print('This is downside hill')
n = 5
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for k in range(i,n):
        print('*',end='')
    for k in range(i,n-1):
        print('*',end='')
    print()

#this is a diamond
print('This is a diamond')
n = 5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    for k in range(i):
        print('*',end='')
    print()

for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for k in range(i,n):
        print('*',end='')
    for k in range(i,n-1):
        print('*',end='')
    print()