n1 = int(input('Enter 1st number :'))
n2 = int(input('Enter 2nd number :'))

if n1>n2:
    min = n2
elif n1<n2:
    min = n1

for i in range(1,min+1):
    if n1%i==0 and n2%i==0:
        hcf= i

print(f'The GCD of {n1} and {n2} is {hcf}')