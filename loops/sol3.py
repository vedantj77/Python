#print the multiplication table for a given number upto10, but skip the 5th iteration

n = int(input('Enter a number : '))

for i in range(1,11):
    print(n,'x',i,'=',n*i)