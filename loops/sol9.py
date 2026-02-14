#

items=['apple','mango','chiku','apple']
newitem=set() #using set is important as list and dictionaries do not support the .add atribute
for item in items:
    if item in newitem:
        print('Duplicate:',item)
        break
    newitem.add(item)