# OOPS - Inheritance
# Demonstrates single level inheritance in Python

class Animal:
    """Base class for animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    """Derived class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

# Creating object
dog = Dog("Buddy", 5, "Golden Retriever")
dog.eat()
dog.sleep()
dog.bark()
