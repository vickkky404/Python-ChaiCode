# OOPS - Properties (Getters and Setters)
# Using @property decorator to create getter and setter methods

class Student:
    """Class demonstrating properties with validation"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name with validation"""
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            print("Invalid name!")
    
    @property
    def age(self):
        """Getter for age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if isinstance(value, int) and 0 < value < 100:
            self._age = value
        else:
            print("Invalid age!")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Usage
student = Student("Alice", 20)
student.display()

# Using property setters
student.name = "Bob"
student.age = 22
student.display()

# Invalid assignment
student.age = 150
