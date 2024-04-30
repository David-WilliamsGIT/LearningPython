# Functions to variables for better understanding

def hello():
    print("Hello")
    
    
#print(hello) # this will print the memory address of the function hello 0x00000234AA5F0CA0

hi = hello
hi() # will print hello event though the function is assigned to hi variable

say = print
say("Printing this text through the variable print")