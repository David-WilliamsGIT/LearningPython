# Simple implementation of inheritance in python

class Animal: # Animal is the parent class of the Rabbit class
    
    alive = True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
    def swim(self):
        print("This animal is swimming")      
                     
    def fly(self):
        print("This animal is flying")
   
        
class Rabbit(Animal): # Rabbit is the child class of the Animal class

    def run(self): # inherited from the animal class
        print("This rabbit is running")
        
class Fish(Animal): # Rabbit is the child class of the Animal class

    def swim(self): # inherited from the animal class
        print("This fish is swimming")
        
class Hawk(Animal): # Rabbit is the child class of the Animal class
    
    def fly(self): # inherited from the animal class
       print("This hawk if flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk() # inherited from the animal class

rabbit.run() # inherited from the animal class
fish.swim() # inherited from the
hawk.fly() # inherited from the animal class

# fish.swim()
# hawk.fly()
# rabbit.sleep()
