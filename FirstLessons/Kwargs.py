# Kwargs are parameters that will pack all the parameters into a dictionary.
# useful for testing functions that can accept a varying number of arguments.

def hello(**kwargs):
    #print("Hello",kwargs["first"] + " " + kwargs["middle"] + " " + kwargs["last"])
    print("Hello ", end="")
    for key,value in kwargs.items(): # prints the key and value of the dictionary
        print(value,end=" ") 
    
    
hello(first="David", middle="John", last="Smith")
