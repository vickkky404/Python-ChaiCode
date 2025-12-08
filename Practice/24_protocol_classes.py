# OOPS Program 24: Protocol Classes (Structural Subtyping)
# Demonstrates Protocol for structural subtyping

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Shape:
    def draw(self) -> str:
        return 'Drawing a shape'

class Circle:
    def draw(self) -> str:
        return 'Drawing a circle'

class Square:
    def draw(self) -> str:
        return 'Drawing a square'

class Printer:
    def draw(self) -> str:
        return 'Printing...'

def render(drawable: Drawable) -> None:
    print(drawable.draw())

if __name__ == '__main__':
    shape = Shape()
    circle = Circle()
    square = Square()
    printer = Printer()
    
    render(shape)
    render(circle)
    render(square)
    render(printer)
    
    print('All objects conform to Drawable protocol')
