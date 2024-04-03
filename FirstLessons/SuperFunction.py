# super() function that allows you to call a method from the parent class.
# this function will return a temporary object of the parent class

class Rectangle: # parent class method
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Square(Rectangle): # child class method
    
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
            return self.length * self.width
        
class Cube(Rectangle): # child class method
        
        def __init__(self, length, width, height):
            super().__init__(length, width)# this makes the difference between cube and square
            # don't need length or width because of the super() function
            self.height = height 
            
        def volume(self):
            return self.length * self.width * self.height

        
        
 
square = Square(3, 3)
rectangle = Rectangle(8, 3)
cube = Cube(3, 3, 3)

print(cube.volume())
print(square.area())
      
      