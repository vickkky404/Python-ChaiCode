# Decorator Pattern

def logged_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def timer_method(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

class Calculator:
    @logged_method
    def add(self, a, b):
        return a + b
    
    @logged_method
    @timer_method
    def multiply(self, a, b):
        return a * b

# Testing
calc = Calculator()
print(calc.add(5, 10))
print()
print(calc.multiply(4, 5))
