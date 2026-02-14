n = int(input('Enter a number to check if its an Armstrong Number :'))

copy = n
sum = 0
order = len(str(n))



while (n>0):
    l_digit = n%10
    sum += l_digit**order
    n= n//10

if sum == copy:
    print(f'{copy} is an ArmStrong Number !')
else:
    print(f'{copy} is not an ArmStrong Number !')