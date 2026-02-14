name = input("Whats your name ? ").strip().title()
print(f"Hello, {name}")


x = float(input("What's x? "))
y = float(input("Whats y? "))

z=round(x+y)
print(z)


#defining a function in python

def bocha(to="locha"):     
    print("Hello, " +to)

bocha() 
name = input("What's your favourite number ?")
bocha(name)  #name = to