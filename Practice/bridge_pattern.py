"""Bridge Pattern - Decouple abstraction from implementation."""
from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius): pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'API1: Circle at ({x},{y}) radius {radius}')

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'API2: Circle at ({x},{y}) radius {radius}')

class Shape(ABC):
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api
    
    @abstractmethod
    def draw(self): pass

class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x, self.y, self.radius = x, y, radius
    
    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

if __name__ == '__main__':
    shapes = [Circle(1, 2, 3, DrawingAPI1()), Circle(5, 7, 8, DrawingAPI2())]
    for shape in shapes:
        shape.draw()
