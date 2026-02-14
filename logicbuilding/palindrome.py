og = input('Enter a string : ')

slice = og[::-1] 
new=slice

if og == new:
    print("The entered string is a palindrome ! ")
else:
    print("The string is not a palindrome.")