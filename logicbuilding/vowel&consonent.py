name = input('Enter any one string :')
name.lower()
vowel =0
consonant =0
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel +=1
    else:
        consonant+=1

print('vowel : ', vowel)
print('consonant : ',consonant)