# args are parameters that will pack all the arguments into a tuple.
# this is useful for when you don't know how many arguments will be passed to the function.

def add(*something): # a good convention for naming the args is to use *args and not *something
    sum = 0
    something = list(something) # casting to list so we can modify the tuple
    something[0] = 0
    for i in something:
        sum += i
    return(sum)

print(add(1,2,3,4,5,6)) # prints the number 20

