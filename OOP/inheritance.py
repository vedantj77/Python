class Pet:      #upperlevel class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")


    def speak(self):
        print('Helllooo')

class Cat(Pet):  #child class
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color= color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def speak(self):        #this method will over-ride the speak method from the upperlevel class when speak method is called from Class Cat
        print("Meow")

class Dog(Pet):     #child class
    def speak(self):
        print("Bark")       #this method will over-ride the speak method from the upperlevel class when speak method is called from Class Dog

class Fish(Pet):
    pass                    #if we use speak method here it will display method from upperlevel class

p=Pet('Billy', 20)
p.show()
p.speak()
c=Cat('Chinki', 5, 'green')
c.show()
c.speak()

f=Fish('SAM',3)
f.speak()