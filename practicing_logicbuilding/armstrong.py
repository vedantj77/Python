n = int(input("Enter a number : "))
power = len(str(n))
sum = 0
copy = n

while (n>0):
    digit = n%10
    sum += digit ** power
    n = n//10 

if (sum == copy):
    print("Armstrong Number !")
else : 
    print("Not an Armstrong Number !")