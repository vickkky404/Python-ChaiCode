# Using Properties (@property decorator)

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """Getter for name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name"""
        if isinstance(value, str):
            self._name = value
        else:
            print("Name must be a string")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if 0 < value < 100:
            self._age = value
        else:
            print("Age must be between 0 and 100")

# Testing
student = Student("Alice", 20)
print(f"Name: {student.name}, Age: {student.age}")
student.name = "Bob"
student.age = 22
print(f"Name: {student.name}, Age: {student.age}")
