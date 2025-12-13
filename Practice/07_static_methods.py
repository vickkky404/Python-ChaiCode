# Static Methods and Class Methods

class MathUtils:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method doesn't use self or cls"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @classmethod
    def circle_area(cls, radius):
        """Class method uses cls parameter"""
        return cls.pi * radius ** 2
    
    @classmethod
    def get_pi(cls):
        return cls.pi

# Testing
print(f"Add 10, 20: {MathUtils.add(10, 20)}")
print(f"Subtract 20, 5: {MathUtils.subtract(20, 5)}")
print(f"Circle area (r=5): {MathUtils.circle_area(5)}")
print(f"Pi value: {MathUtils.get_pi()}")
