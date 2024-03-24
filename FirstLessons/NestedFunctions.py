# Nested functions are function calls inside of other functions. 
# They are useful for breaking down complex problems into smaller, more manageable parts.

print(round(abs(float(input("Enter a number: "))))) # this will print the number rounded 
#to the nearest whole number

# the above code can be broken down into smaller parts using nested functions
# below is the longer version of it.

# num = input("Enter a number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)