# map function applies a function to each item in an iterable (list, tuple, etc.)

# map(function, iterable)

store = [("Axe", 200),
         ("Sword", 150),
        ("Bow", 100),
        ("Staff", 50),
        ("Dagger", 75)]

# converting euros to dollars, 1 euro = 1.07 dollars
to_dollars = lambda data: (data[0], data[1]*1.07)
#to_euros = lambda data: (data[0], data[1]/1.07)

store_dollars = list(map(to_dollars, store))
#print(store_dollars)

for i in store_dollars:
    print(i)