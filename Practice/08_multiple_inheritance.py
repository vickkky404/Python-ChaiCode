# OOPS - Multiple Inheritance
# Demonstrates multiple inheritance in Python using MRO

class Animal:
    """First parent class"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} is moving")

class Swimmer:
    """Second parent class"""
    
    def swim(self):
        print(f"{self.name} is swimming")

class Flyer:
    """Third parent class"""
    
    def fly(self):
        print(f"{self.name} is flying")

class Duck(Animal, Swimmer, Flyer):
    """Child class inheriting from multiple parents"""
    
    def quack(self):
        print(f"{self.name} says: Quack!")

# Usage
duck = Duck("Donald")
duck.move()
duck.swim()
duck.fly()
duck.quack()

# MRO - Method Resolution Order
print("\nMRO of Duck class:")
for cls in Duck.__mro__:
    print(f"  {cls.__name__}")
