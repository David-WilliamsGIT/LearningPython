# Index operators give access to the sequence's elements such as (str,list,tuples)

name = "david williams"

if (name[0].islower()):
    name = name.capitalize()
    
correction = (name[0] + "avid " + name[6].upper() + "illiams") # This will correctly spell David Williams
# adding capitals to the name where there should be.   
print(correction)

#new_name = "John Henkrikson"

# correct_name = new_name.replace(new_name[0], 'Y') # Will replace the first letter of the name with 'Y'
# print(correct_name)

# corrected_nameTwo = new_name.replace(new_name[0:15], 'Tannu') # replaces the full name with 'Tannu'
# print(corrected_nameTwo)

# friends_name = "Julie"

# correction = friends_name.replace(friends_name[0:5], 'Ghoulie') # replaces the full name with 'Ghoulie'
# print(correction)