n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

if n2>n1:
    min=n1
else:
    min=n2

for i in range(1,min+1):
    if n1%i==0 and n2%i==0:
        hcf=i

print(f"The HCF/GCD of these 2 numbers is {hcf} ")