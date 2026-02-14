a,b,c,d,e =map(int,input('Enter marks of 5 papers :').split())
total=a+b+c+d+e
percentage = total/5.0
print('Total marks : ',total)
print('Percentage : ',percentage)
if a >= 40 and b >= 40 and c >=40 and d >=40 and e >=40:
    print('pass')
else:
    print('fail')
