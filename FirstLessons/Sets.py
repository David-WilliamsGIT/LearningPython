# Sets are collections of strings, numbers, or other objects. They are unordered and unindexed.

utensils = {"fork", "spoon", "knife", "blender"}
dishes = {"bowl", "plate", "cup"}

dishes.add("pots") # adding an item to the set.
utensils.remove("blender")
utensils.add("Mug") # adding an item to the set
print(utensils)


items = [utensils, dishes] # combine together so that when printing, it will print all items.

for x in items: # for loop to print all items in the list.
    for items in x: # 
        print(items)
        