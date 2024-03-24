# Exceptions are events detected during the execution of a program that disrupt the normal flow of instructions.
# They are handled using try and except blocks.

# This program will casuse and exception
try:
    numerator = int(input("Enter a number to divide by: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something went wrong, :( ")
else:
    print(result)
finally: # finally passes whether or not an exception is raised or not
    print("This will always run")