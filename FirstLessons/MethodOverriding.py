# A simple method overriding program

class Animal:
    
    def eat(self):
        print("Animal is eating.")

class Rabbit(Animal):
    
    def eat(self): # This method will override the method from Animal class
        print("Rabbit is eating a carrot.")
        
        
rabbit = Rabbit()
rabbit.eat()