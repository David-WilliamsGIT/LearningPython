# list comprehension is a way to create a list in Python with less syntax. 
# It is a concise way to create a list by iterating over an iterable object and can mimic lambda functions.

# example
# numbers = []
# for i in range(1, 15):
#     numbers.append(i * i)
# print(numbers)

# the list comprehension way to write the above code
numbers = [i * i for i in range(1, 15)]
print(numbers)

students = [100,90,70,50,60,40,30,20,0]

# passed_students = list(filter(lambda x: x >= 50, students))
# print(passed_students)

# the list comprehension way to write the above code
#passed_students = [x for x in students if x >= 50]
#print(passed_students)

passed_students = [x if x >= 50 else "Failed" for x in students]
print(passed_students)