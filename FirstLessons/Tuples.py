# Tuples in python are not supported by the list data structure. 
# They are immutable and are defined by using parentheses.
# they are a collection of elements that are ordered and unchangeable.
# They are also used to group together related data structures.

student = ("David", 35, "Male")
#print(student)

for x in range(len(student)):
    print(student[x])


# print(student.count("David"))
# print(student.index("David"))

if 36 in student:
    print("There is a student who is 35 years old.")
else:
    print("There is no student who is 35 years old.")