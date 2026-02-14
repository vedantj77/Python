n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))

maxNum = max(n1,n2)

while(True):
    if maxNum%n1 == 0 and maxNum%n2 == 0:
        break
    maxNum +=1

print("LCM :", maxNum)