# Iterator Protocol

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

class FibonacciIterator:
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

# Testing
print("CountUp to 5:")
for num in CountUp(5):
    print(num, end=' ')

print("\n\nFibonacci up to 50:")
for fib in FibonacciIterator(50):
    print(fib, end=' ')
print()
