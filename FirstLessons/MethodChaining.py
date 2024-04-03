# Method chaining is calling multiple methods sequentially

class Car:
    
    def turn_on(self):
        print('The car was turned on')
        return self
    
    def drive(self):
        print('The car is driving')
        return self
        
    def brake(self):
        print('The car is braking')
        return self
        
    def turn_off(self):
        print('The car is turned off') 
        return self
        
car = Car()
car.turn_on().drive().brake().brake().turn_off() # this is the method chaining

