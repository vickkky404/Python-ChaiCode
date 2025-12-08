# OOPS Program 25: Callable Objects
# Demonstrates making objects callable using __call__

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

class Logger:
    def __init__(self, prefix='LOG'):
        self.prefix = prefix
        self.count = 0
    
    def __call__(self, message):
        self.count += 1
        print(f'[{self.prefix}:{self.count}] {message}')

class Pipeline:
    def __init__(self):
        self.functions = []
    
    def add(self, func):
        self.functions.append(func)
        return self
    
    def __call__(self, value):
        for func in self.functions:
            value = func(value)
        return value

if __name__ == '__main__':
    double = Multiplier(2)
    triple = Multiplier(3)
    
    print('double(5):', double(5))
    print('triple(5):', triple(5))
    
    logger = Logger('DEBUG')
    logger('Starting application')
    logger('Processing data')
    
    pipe = Pipeline()
    pipe.add(lambda x: x * 2).add(lambda x: x + 10).add(lambda x: x ** 2)
    print('Pipeline result:', pipe(5))
