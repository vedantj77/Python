word = input("Enter the word : ")
naam = ""
for i in word:
    if i in naam:
        continue
    naam +=i

print(naam)