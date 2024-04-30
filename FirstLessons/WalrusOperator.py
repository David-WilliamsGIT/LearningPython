# walrus operator :=

# assignment expression that assigns values to vartiables as part of a larger expression

# the normal way to write the expression
# happy = True
# print(happy)

# the walrus operator way to write the expression
#print(happy := True)

# foods = list()
# while True:
#     food = input("What food would you like to eat?: ")
#     if food == "quit":
#         break
#     foods.append(food)
#     print(foods)
    
# the walrus operator way to write the expression
foods = list()
while food := input("What food would you like to eat?: ") != "quit":
    foods.append(food)
    print(foods)
    

