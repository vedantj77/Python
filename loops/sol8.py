#check prime number or not
n = int(input())
if n<2 :
    print('Not a prime number.')
else:
    for i in range(2,n):
        if n%i==0:
            print('Not a prime number.')
            break
    else:
        print('Number is prime.')