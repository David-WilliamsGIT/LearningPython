# A program based on abstract classes that are used to define a blueprint for other classes.

# Prevents a user forom creating an object of that class
# abstract class = a class which contains one or more abstract methods
# abstract method = a method that is declared, but contains no implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go (self):
        pass
    
    @abstractmethod
    def stop (self):
        pass
    
class Car(Vehicle):
    def go(self):
        print("You drive the car")
        
    def stop (self):
        print("This car is stopped")
        
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
        
    def stop (self):
        print("This motorcycle is stopped")    
    
#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
