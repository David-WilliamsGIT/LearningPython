# Dictionaries are a changable, unordered collection of key-value pairs. 
# They are indexed and written with curly brackets. Dictionaires are fast
# because they use hash tables to store data.

people =     {'David': 'Rosslair', 
              'John':  'Carlow', 
              'Paul':  'Cork', 
              'George':'Galway', 
              'Ringo': 'Belfast'} # dictionary with key-value pairs.


# print(people['David']) # prints the value of the key 'David' which will print 'Rosslair'

# print(people.get('Andrew')) # will print none as there is no 'Andrew' key in the dictionary
# # this is to show you can search for something in the dictionary without getting an error.

# print(people.keys()) # prints the keys of the dictionary
# print(people.values()) # prints the values of the dictionary


for key, value in people.items():
    print(key, value) # prints the keys and values of the dictionary
    
people.update({'Julie': 'Newbridge'}) # adds a new key-value pair to the dictionary
people.update({'John': 'Naas'}) # updates the value of the key 'John' to 'Naas'
print(people) # adds a new key-value pair to the dictionary



    
    
    