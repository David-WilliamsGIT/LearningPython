# While loops are loops that can be executed a block of code, as long as a condition is true.

# first example is an example of an infinite loop,
# this happens when you don't have a condition that will eventually be false.
#while 1 == 1:
#    print("Help, I am stuck in this loop!")


# now for a read while loop condition that will be met when a condition is true

# name = input("Please enter your name: ")

# code below is a joke I send to my friend who likes to type kk.
# if name == "John":
#     kk = input("Did John tpye kk in discord? ")
#     if kk == "yes" or kk == "Yes":
#         print("John is a borderline member of the KKK group!")
        
# print("Hello " + name + "!" + " of the KKK group!")

# ctrl + / is multi line commenting

name = ""
while len(name) == 0:
    name = input("Please enter your name: ")
    
print("Hello " + name + "!")

# alternative to the above code

# nameTwo = None

# while not nameTwo:
#     nameTwo = input("Enter your name: ")
    
# print("Hello " + nameTwo)

