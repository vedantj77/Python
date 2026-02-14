#reverse a string using loop

name = input('Enter a name')
reversedname = ""
for i in name:
    reversedname = i + reversedname

print(reversedname)