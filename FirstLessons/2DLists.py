# 2D lists are lists of lists. They are used to store data in a grid format.

drinks = ["Beer", "Coke", "Water", "Orange Juice", "Milk"]
dinner = ["Pizza", "Burger", "Fries", "Salad", "Pasta"]
desserts = ["Ice Cream", "Cake", "Pie", "Donuts", "Cupcakes"]

food = [drinks, dinner, desserts]

print(food[0][1], food[1][3], food[2][3]) # Will print something from each list (drinks, dinner, desserts)