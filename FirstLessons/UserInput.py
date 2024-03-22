# User input fields in python

name = input("What is you name?: ")
age = input("What is your age?: ")
height = input("What is your height?: ")
whereFrom = input("What is your from?: ")
castFloat = float(input("What is a float number? "))

print("Hello " + name + " Who is " + age + " Years old with a height of " + height + "cm and is from " + whereFrom)
print("This is what a float number looks like: " + str(castFloat))