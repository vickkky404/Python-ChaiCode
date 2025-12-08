# OOPS Program 14: Abstract Base Classes
# Demonstrates abstract classes and methods using ABC module

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def display(self):
        print('This is a shape')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    circle = Circle(5)
    print(f'Circle Area: {circle.area()}')
    print(f'Circle Perimeter: {circle.perimeter()}')
    circle.display()
    
    rect = Rectangle(4, 6)
    print(f'Rectangle Area: {rect.area()}')
    print(f'Rectangle Perimeter: {rect.perimeter()}')
    rect.display()
