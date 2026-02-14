#keep asking user for input until they enter a number between 1 to 10
while True:
    n = int(input('Enter a number between 1-10 : '))
    if 1<=n<=10:
        print('Correct')
        break
    else:
        print('Invalid input !')