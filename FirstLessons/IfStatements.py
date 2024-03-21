# If statements in python, they are conditional statements that execute if the statement is true or false


age = int(input("How old are you?: "))

if age <= 0:
    print("How do you exists? what is your secret? what even are you? :O")
elif age > 0 and age < 18:
    print("You are still not an adult yet")
elif age == 18:
    print("You are an adult now. You can go drink alcamaholze now!")
elif age >= 20 and age <= 30:
    print("You are now an adult who needs a job. Also get out of your moms basement.")
elif age >= 31 and age <= 64:
    print("You are a middle aged person living the loife")
elif age >= 65 and age <= 75:
    print("You are ready to retire!")
elif age > 75 and age < 95:
    print("Ok you are getting really old and should probably really retire now and do fun things")
elif age > 95:
    print("ok you are old AF, time to go to the retirement home and play bingo.")
else:
    print("You are to old to exist, begone demon!")
      