# String slicing is when you want to slice a string into a substring.
# to do this, you need to use indexing[] or slice()
# an example of this would be: string[0:3] or string[0:3:1] and slice() string.slice(0, 3, 1) also [start: stop:step]


name = "David Williams"

first_name = name[0:5] # first index is inclusive, and last index is exclusive 
last_name = name[6:14]
print(first_name + " " + last_name)

weird_name = name[0:14:2] # this will make "print" every second letter in the string, change the 2 to a 3 for every third letter in the string
print(weird_name)

new_name = "David Williams"

split_name = new_name.split(" ")
print(split_name[0]) # splits the name into a list of strings, and prints the first element in the list


reversed_name = another_new_name = name[::-1] # this will reverse the string
print(reversed_name)

website = "https://www.google.com"

sliced_website = slice(12,-4) # this will slice the website from the 12th index to the 4th index from the end
print(website[sliced_website]) # prints the website from the 12th index to the 4th index from the end printing google
