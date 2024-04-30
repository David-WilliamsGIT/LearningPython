# Duck typing = where the class of an object is less important than the methods class type
# is not checked if minimum methods are present


class Duck:
    
    def walk(self):
        print("The duck is walking")
        
    def talk(self):
        print("The duck is quacking")
        
class Chicken:
    
    def walk(self): # if remove this method, the catch method will not work
        print("The chicken is walking")
        
    def talk(self):
        print("The chicken is clucking")
        
class Person:
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("The person caught the duck")
        
    def catch(self, chicken):
        print("The person caught the chicken")
        
        
        
chicken = Chicken()
duck = Duck() 
person = Person()

person.catch(chicken)

