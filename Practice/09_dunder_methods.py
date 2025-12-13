# Dunder (Magic) Methods

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# Testing
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
