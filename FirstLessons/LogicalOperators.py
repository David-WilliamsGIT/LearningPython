# logical operators (AND, OR, NOT) used to check if 
# two or more conditions are true or false

tempurature = int(input("What is the temperatue outside? "))

if tempurature < 0:
    print("The temperature " + str(tempurature) + " celcius, it is freezing outside")
elif tempurature >= 0 and tempurature <= 10:
    print("The temperature is " + str(tempurature) + " celcius outside")
else:
    print("The temperature is " + str(tempurature) + " celcius, it is very hot outside")
