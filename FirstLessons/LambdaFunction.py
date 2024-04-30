# Lambda function = A function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression
# think of it as a shortcut and is useful if needed for short periods of time


# the normal way to write a function
# def double(x):
#     return x * 2


double = lambda x: x * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(5, 6))
add = lambda x, y, z: x + y + z
print(add(5, 10, 22))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name(input("what is your first name? "), input("what is your last name? ")))
age_check = lambda age: (True, "is 18") if age == 18 else (True, "Is older than 18") if age > 18 else (False, "Is younger than 18")
print(age_check(int(input("what is your age? "))))
