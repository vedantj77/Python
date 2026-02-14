#id is used to show the address of elements

name = 'Vedant'
print(id(name))

#in python if the values of 2 variables are same then they both will point to same address box
a = 10
b = a 
print(id(a))
print(id(b))
print(id(10))

#to display data type
hell = 65
print(type(hell))

#typecasting
a = 5.6
b = int(a)
print(type(a))
print(type(b))
print(b)
#complex datatype in python 
x=7
y=8
z= complex(x,y)
print(z)

#range in python can take 3 values and the last one is the difference
print(list(range(2,10,2)))


#multiline string 
s="""hello
bocha       
locha """
print(s[0])
print(s)

#using eval function
result= eval(input('Enter an expression'))
print(result)



