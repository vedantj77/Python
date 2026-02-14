n = int(input("Enter the range of fibonacci series : "))
a = 0
b =1
sum=1

if n == 1:
    print(a)
    print("Sum : 0")
elif n == 2:
    print(b)
    print("Sum : 1")
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        sum += c
        print(c)
        a=b
        b=c
    print("Sum is : ", sum)

