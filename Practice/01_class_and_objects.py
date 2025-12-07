# OOPS - Class and Objects
# A basic class example demonstrating class definition and object creation

class Person:
    """A simple class to represent a person"""
    
    def __init__(self, name, age):
        """Constructor to initialize person attributes"""
        self.name = name
        self.age = age
    
    def display_info(self):
        """Method to display person information"""
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
person1 = Person("Raj", 20)
person2 = Person("Priya", 22)

# Accessing methods
person1.display_info()
person2.display_info()
