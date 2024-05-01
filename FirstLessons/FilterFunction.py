# filter() is a function that creates a collection of elements from an iterable for which a function returns true.

# fitler(function, iterable)

friends = [("John", 36),
           ("Jane", 30),
           ("Jack", 25),
           ("Jill", 29),
           ("Jim", 40),
           ("Jenny", 28),
           ("Jerry", 35)]

age = lambda data: data[1] >= 26 and data[1] <= 35

not_real_friends = list(filter(age, friends))

for i in not_real_friends:
    print(i)