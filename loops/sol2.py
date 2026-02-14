#calculate the sum of even numbers up to a given number n
n = int(input('Enter a number : '))
count=0
sum=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
        sum+=i
print('The count of even numbers uptill',n,'is :',count)
print('The sum of even numbers uptill',n,'is :',sum)