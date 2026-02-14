#given a string, find the first non-repeated character using while loop
input_str = 'teeteracac'

for i in input_str:
    print(i)
    if input_str.count(i) == 1:
        print('Char is : ', i)
        break #after finding the first character it willstop thats why break is used