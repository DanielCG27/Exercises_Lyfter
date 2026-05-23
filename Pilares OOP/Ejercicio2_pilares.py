from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print(f"The circle area is: {area}")
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The circle perimeter is: {perimeter}")
        return perimeter
        
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print(f"The rectangle area is: {area}")
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        print(f"The rectangle perimeter is: {perimeter}")
        return perimeter
        

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        area = self.side_length ** 2
        print(f"The square area is: {area}")
        return area
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side_length
        print(f"The square perimeter is: {perimeter}")
        return perimeter
    

circle = Circle(25)
circle.calculate_area()
circle.calculate_perimeter()

rectangle = Rectangle(15, 8)
rectangle.calculate_area()
rectangle.calculate_perimeter()

square = Square(65)
square.calculate_area()
square.calculate_perimeter()        