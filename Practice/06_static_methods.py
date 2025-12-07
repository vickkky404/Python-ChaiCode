# OOPS - Static Methods and Class Methods
# Demonstrates static and class methods in Python

class MathOperations:
    """Class demonstrating static and class methods"""
    
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't require instance or class"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Another static method"""
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method - receives class as first argument"""
        print(f"Using pi value: {cls.pi}")
        return a * b
    
    @classmethod
    def from_string(cls, string_value):
        """Class method for alternative constructor"""
        a, b = map(float, string_value.split(','))
        return cls.add(a, b)

# Using static methods
print(f"Add: {MathOperations.add(10, 5)}")
print(f"Subtract: {MathOperations.subtract(10, 5)}")

# Using class methods
print(f"Multiply: {MathOperations.multiply(10, 5)}")
result = MathOperations.from_string("3.5,2.5")
print(f"Sum from string: {result}")
