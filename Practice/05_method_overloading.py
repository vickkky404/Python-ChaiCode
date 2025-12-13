# Method Overloading in Python
# Using default arguments and variable arguments

class Calculator:
    def add(self, a=0, b=0, c=0):
        """Add two or three numbers"""
        return a + b + c
    
    def multiply(self, *args):
        """Multiply any number of arguments"""
        result = 1
        for num in args:
            result *= num
        return result
    
    def power(self, base, exponent=2):
        """Calculate power with default exponent"""
        return base ** exponent

# Testing
calc = Calculator()
print(f"Add 5, 10: {calc.add(5, 10)}")
print(f"Add 5, 10, 15: {calc.add(5, 10, 15)}")
print(f"Multiply 2, 3, 4: {calc.multiply(2, 3, 4)}")
print(f"Power 2 (default): {calc.power(2)}")
print(f"Power 2^5: {calc.power(2, 5)}")
