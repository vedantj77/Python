n = int(input("Enter the number : "))
sum=0
order=len(str(n))
copy= n

while(n>0):
    digit=n%10
    sum += digit**order
    n= n//10


if(sum== copy):
    print(copy, "is an armstrong number ! ")
else:
    print(copy," is not an armstrong number. ")