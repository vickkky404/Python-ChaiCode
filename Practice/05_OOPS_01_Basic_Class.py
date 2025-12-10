# OOPS Program 1: Basic Class and Object
# Create a simple Person class with attributes and methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

# Create objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Display info
person1.display_info()
person2.display_info()

# Call method
person1.birthday()
