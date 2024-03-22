# For loops are statements just like while loops that will execute it's block of code, but
# unlike while loops, for loops execute code a limited number of times

# while loops = infinite
# for loops = limited

import time

# for i in range(10):
#     print(range(i)) # will print 0 - 9
#     print(range(i + 1)) # will print 1 - 10

# for i in range(10, 100):
#     print(range(i)) # will print 10 to 99

# for i in range(10, 100+1, 2):
#     print(range(i)) # this will count up by 2's starting from 10

# for i in "David Williams":
#     print(i) # this will print the name David Williams
    
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1) # sleep for 1 second
    
print("Happy new project!") 