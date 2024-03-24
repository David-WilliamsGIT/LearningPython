# String formating is an optional method that can be used to format strings in a more readable way.

#---------------------------------------------------------------------------------------------------#
# Number formating
# number = 1000

# print("The number of pi is {:.3f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))

#---------------------------------------------------------------------------------------------------#
animal = "Cow"
item = "Moon"

#print("The {} jumped to the {}".format(animal, item))
#print("The {animal} jumped to the {item}".format(animal="Cow", item="Moon",)) # keyword arguments

# A more elegant way to use the string formating
text = "The {} jumped to the {}"
print(text.format(animal, item))


#---------------------------------------------------------------------------------------------------#
# name formatting
name = "David"
print("Hello, my name is {}".format(name)) 
print("Hello, my name is {:10}. Have a nice day".format(name)) # padding to the right of the string
print("Hello, my name is {:>10}. Have a nice day".format(name)) # padding to the left of the string
print("Hello, my name is {:<10}. Have a nice day".format(name)) # padding to the right of the string
print("Hello, my name is {:^10}. Have a nice day".format(name)) # padding to the center of the string
print("Hello, my name is {:_^10}. Have a nice day".format(name)) # padding to the center of the string
print("Hello, my name is {:_<10}. Have a nice day".format(name)) # padding to the right of the string
print("Hello, my name is {:_>10}. Have a nice day".format(name)) # padding to the left of the string

#---------------------------------------------------------------------------------------------------#