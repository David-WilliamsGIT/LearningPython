# Keyword arguments are arguments preceded by and identifier when we pass them to a function. 
# The order of the arguments doesn't matter, unlike positional arguments.

def hello(first,middle,last):
    print("Hello",first,middle,last)
    
hello(first="John",middle="Fitzgerald",last="Kennedy")
