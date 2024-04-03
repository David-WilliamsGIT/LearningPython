# Multi-level inheritance is when a child class inherits from another child class.

class Organism: # Parent class
    
    alive = True
    
class Animal(Organism): # child class Animal
    
    def eat(self):
        print("This animal is eating.")
        
class Dog(Animal): # derived child class that inherits from the Animal child class
    
    def bark(self):
        print("This dog is barking.")
        
dog = Dog() 
print(dog.alive) # printing true from parent class Organism
dog.eat()  # using the eat function from the Animal class
dog.bark() # using the bark function from the Dog class