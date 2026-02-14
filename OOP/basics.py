class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    #modifying attributes i.e to change the value passed in a method
    def set_age(self,age):
        self.age = age

    #this is a method
    def bark(self):
        print('bark')

d=Dog("Tommy",3) #d here is an object of type Dog
d.set_age(10)
print(d.get_name())
print(d.get_age())

d1=Dog('Wolly', 5)
print(d1.get_name())
print(d1.get_age())

d.bark() #bark is a method of an object d which can be called by d.bark()
