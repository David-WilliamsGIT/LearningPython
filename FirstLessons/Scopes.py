# scopes in python are the region that a variable is defined and can be used.
# the variable cannot be used outside of the scope it is defined in.

name = "David" # global variable, global scope.

def display_name(): # function to display the name of the variable defined within the scope of the function
    name = "Williams"
    print(name)

print(name) # this will print David which is out of the display_name() function scope
display_name() # this will print Williams which is inside the display_name() function scope

