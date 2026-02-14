def highestSalary(mydict):
    max=0
    name=''
    for i in mydict.values():
        if i > max:
            max = i

    
            
    return max
mydict = {'Prashant jha' : 200000, 'Vedant Jadhav': 3000000,'Ashish ':40000}

print(highestSalary(mydict))