# OOPS Program 23: Bound and Unbound Methods
# Demonstrates bound and unbound method concepts

class Calculator:
    def __init__(self, initial=0):
        self.value = initial
    
    def add(self, x):
        self.value += x
        return self.value
    
    def subtract(self, x):
        self.value -= x
        return self.value
    
    @staticmethod
    def static_add(a, b):
        return a + b
    
    @classmethod
    def create_from_string(cls, value_str):
        return cls(int(value_str))

if __name__ == '__main__':
    calc = Calculator(10)
    
    bound_add = calc.add
    print('Bound method result:', bound_add(5))
    
    unbound_add = Calculator.add
    print('Unbound method result:', unbound_add(calc, 3))
    
    print('Static method:', Calculator.static_add(20, 30))
    
    calc2 = Calculator.create_from_string('100')
    print('Class method created:', calc2.value)
