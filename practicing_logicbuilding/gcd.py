n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd Number : "))

minNum = min(n1,n2)
TheNum = ""

for i in range(1,minNum+1):
    if n1%i==0 and n2%i==0:
        TheNum = int(i)

print("HCF : ", TheNum)
