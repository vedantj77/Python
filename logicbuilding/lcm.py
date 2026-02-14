n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

maxNum = max(n1,n2)

#while(True): An infinite loop that will keep running until the condition inside is satisfied.
while(True):
    if( maxNum%n1==0 and maxNum%n2==0):
        break
    maxNum += 1
#This checks whether maxNum is divisible by both n1 and n2 (i.e., no remainder when dividing maxNum by n1 and n2).
#if the condition is true, the loop stops (break).
#If the condition is false, maxNum is incremented by 1:

print(f"The lcm of {n1} and {n2} is {maxNum}")
