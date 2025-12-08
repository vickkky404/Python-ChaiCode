# OOPS Program 28: Iterator Protocol
# Demonstrates __iter__ and __next__ methods

class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a <= self.limit:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    print('CountUp to 5:')
    for num in CountUp(5):
        print(num, end=' ')
    
    print('\nFibonacci up to 50:')
    for num in Fibonacci(50):
        print(num, end=' ')
