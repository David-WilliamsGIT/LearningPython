# Loop Control Statements are used to change a loops execution from its normal sequence
# Examples:
# break is used to terminate the loop completely
# continue is used to continue to the next iteration of the loop
# pass is used to do nothing, is a placeholder

# Loop with a break control statement
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
    
# Loop with a continue control statement
# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")
    
# Loop with a pass control statement
for i in range(1, 11):
    if i == 7:
        pass # this will pass the number 7 when the loop is executed
    else:
        print(i, end="")