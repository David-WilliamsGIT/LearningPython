# Nested loops are the "inner" loop that will finish all of it's iterations before
# finishing the outer loop

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("What symbol do you want")
    
    
#-------------------------------(First nested loop)-------------------------------#    
# now for a triangle 
# the two nested loops below will aim to print a pyramid using 5 rows and 5 columns
for i in range(rows):
    for j in range(i + 1):
        print(symbol, end="")
    print()

#this code will print this part of the triangle
# *
# **
# ***
# ****
# *****

#-------------------------------(Second nested loop)------------------------------#

# (Second nested loop)
for i in range(rows - 1, 0, -1): # this will print the rows in reverse order starting from 4
    for j in range(i):
        print(symbol, end="")
    print()

# this will print this part of the triangle completing the full pyramid
# ****
# ***
# **
# *

#-------------------------------(Third nested loop)-------------------------------#
#combining the two nested loops from above into one
# for i in range(1, 2*rows):
#     if i <= rows:
#         for j in range(i):
#             print(symbol, end="")
#     else:
#         for j in range(2*rows - i):
#             print(symbol, end="")
#     print()

#-------------------------------(Fourth nested loop)-------------------------------#
# this will print out the rows and colums with the symbol, 
# example 5r, 5c will print ***** 5 times
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
        
#     print()

#-------------------------------(Fifth nested loop)-------------------------------# 
# code below prints a really cool image! (works with the very first nested loop)
# for i in range(i + 6):
#     for j in range(j + i - 1):
#         print(symbol, end="")
#     print()  

# *
# **
# ***
# ****
# *****
# ***
# **
# **
# ***
# *****
# ********
# ************
# *****************
# ***********************
# ******************************
#--------------------------------------------------------------------------------#