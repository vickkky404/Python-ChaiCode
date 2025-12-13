# Operator Overloading

class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        return Money(self.amount - other.amount)
    
    def __mul__(self, factor):
        return Money(self.amount * factor)
    
    def __truediv__(self, factor):
        return Money(self.amount / factor)
    
    def __lt__(self, other):
        return self.amount < other.amount
    
    def __gt__(self, other):
        return self.amount > other.amount
    
    def __eq__(self, other):
        return self.amount == other.amount
    
    def __str__(self):
        return f"${self.amount:.2f}"

# Testing
m1 = Money(100)
m2 = Money(50)
print(f"m1: {m1}, m2: {m2}")
print(f"m1 + m2 = {m1 + m2}")
print(f"m1 - m2 = {m1 - m2}")
print(f"m1 * 2 = {m1 * 2}")
print(f"m1 / 2 = {m1 / 2}")
print(f"m1 > m2: {m1 > m2}")
print(f"m1 == m2: {m1 == m2}")
