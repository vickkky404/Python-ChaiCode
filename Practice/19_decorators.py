# OOPS Program 19: Decorators
# Demonstrates class decorators and method decorators

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} completed')
        return result
    return wrapper

def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start:.4f} seconds')
        return result
    return wrapper

class MathOperations:
    @log_decorator
    def add(self, a, b):
        return a + b
    
    @log_decorator
    @timing_decorator
    def multiply(self, a, b):
        return a * b
    
    @staticmethod
    @log_decorator
    def divide(a, b):
        return a / b if b != 0 else 'Division by zero'

if __name__ == '__main__':
    math = MathOperations()
    print('Result:', math.add(5, 3))
    print('Result:', math.multiply(4, 5))
    print('Result:', MathOperations.divide(10, 2))
