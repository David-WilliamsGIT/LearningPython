# A program about sorting iterables
# iterables are an iterable object like a list, tuple, or dictionary

# sort() method is used with lists
# sort() function is used with iterables

students = ["Minsc", "Minthara", "Karlach", "Shadowheart", "Gale", "Astarion", "Lae'zel"]
# students = ("Minsc", "Minthara", "Karlach", "Shadowheart", "Gale", "Astarion", "Lae'zel") sort() method does not work with tuples
studentsTwo = ("Minsc", "Minthara", "Karlach", "Shadowheart", "Gale", "Astarion", "Lae'zel")


sorted_studentsTwo = sorted(studentsTwo)

# for i in sorted_studentsTwo:
#     print(i)

#students.sort()
students.sort(reverse=True)

# for i in students:
#     print(i)
    

    
#----------------------------------------------------------------#
#                   Level Two

# list of tuples
studentsThree = [("Minsc", "barbarian", 67),
                ("Minthara", "cleric", 100),
                ("Karlach", "barbarian", 30),
                ("Shadowheart", "cleric", 30),
                ("Gale", "wizard", 40),
                ("Astarion", "rogue", 239),
                ("Lae'zel", "fighter", 20)]


studentsThree.sort()

# for i in studentsThree:
#     print(i)
    
role = lambda student: student[1]
studentsThree.sort(key=role)

for i in studentsThree: # this will pring the students in alphabetical order by their role
    print(i)