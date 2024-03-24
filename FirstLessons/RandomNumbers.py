#Random number utilising, import random module for generating random numbers.

import random

x = random.randint(0, 6) # generates a random number between 0 and 6
y = random.random() # generates a random floating point number

myList = ['Rock', 'Paper', 'Scissors']
z = random.choice(myList) # randomly selects an item from the list

print(x) # prints the random number
print(y) # prints the random float number
print(z) # prints the random string

cards = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
random.shuffle(cards)

print(cards) # prints the random card