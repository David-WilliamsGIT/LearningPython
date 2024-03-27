# A object orientated program in python
import sys

from Car import Car

car_1 = Car("Toyota","Corolla",2019,"Red")
car_2 = Car("BMW", "X5", 2019,"Red")

print(car_1.make, car_1.model, car_1.year, car_1.color)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()