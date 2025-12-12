# Core Python OOPS Program 1: Basic Class and Object
# Demonstrate class creation with attributes and methods

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
    
    def increase_age(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

# Create objects
if __name__ == "__main__":
    person1 = Person("Raj", 20, "raj@example.com")
    person2 = Person("Priya", 22, "priya@example.com")
    
    person1.display_info()
    print()
    person2.display_info()
    print()
    person1.increase_age()
