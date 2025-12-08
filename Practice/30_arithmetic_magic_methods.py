# OOPS Program 30: Arithmetic Magic Methods
# Demonstrates __add__, __sub__, __mul__, __truediv__, etc.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __repr__(self):
        return f'{self.real}+{self.imag}j'

if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print('v1:', v1)
    print('v2:', v2)
    print('v1 + v2:', v1 + v2)
    print('v1 - v2:', v1 - v2)
    print('v1 * 2:', v1 * 2)
    print('v1 / 2:', v1 / 2)
    print('|v1|:', abs(v1))
    
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    print('c1 + c2:', c1 + c2)
