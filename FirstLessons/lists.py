# Lists are use to store mutliple items in a single variable.

food = ["Noodles", "Rice", "Beans", "Ham", "Eggs"]

#print(food) # will print all the elements of the list stored in food
#print(food[3]) # will print at the index set to

#food[0] = "Sushi"

#print(food[0]) # will print sushi

# for x in food:
#     print(x) # will print all the elements of the list stored in food
    
    
food.append("Pizza") # will add pizza to the end of the list
#food.remove(food[2]) # will remove the element at index 2 (beans)
#food.pop() # will remove the element at index
food.insert(3, "Spahgetti") # will insert spahgetti at index 3
food.sort() # will sort the list according to alphabetical order
#food.clear() # will clear the list

print(food) 