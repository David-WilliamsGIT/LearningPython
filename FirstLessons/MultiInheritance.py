# Multiple inheritance is when a child class is derived from more than one parent class

# fish can inherit from prey and predator classes which are parent classes

class Prey:
    
    def flee(self):
        print("The animal flees from the predator")
        
class Predator:
    
    def hunt(self):
        print("The predator is hunting for prey")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()