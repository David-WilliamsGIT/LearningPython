# zip function will aggregate elements from two or more iterables (i.e lists, tuples, etc) 
# and return a zip object with paired elements stored in tuples for each element

# zip(*iterable)


username = ["Dude", "Bro", "Guy"]
passwords =("Password", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

# users = zip(username, passwords) # this is a zip object, print(type(users)) proves this

# users = list(zip(username, passwords)) # casting zip as a list type

# for i in users:
#     print(i)

# users = dict(zip(username, passwords))

# print(type(users))

# for i in users.items():
#     print(key+" : "+value)

users = zip(username, passwords, login_date)
for i in users:
     print(i)