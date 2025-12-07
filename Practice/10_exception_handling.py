# OOPS - Exception Handling
# Demonstrates custom exceptions and exception handling

class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NegativeSalaryError(Exception):
    """Custom exception for negative salary"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Employee:
    """Class demonstrating exception handling"""
    
    def __init__(self, name, age, salary):
        self.name = name
        self.set_age(age)
        self.set_salary(salary)
    
    def set_age(self, age):
        """Set age with validation"""
        if age < 18 or age > 65:
            raise InvalidAgeError("Age must be between 18 and 65")
        self.age = age
    
    def set_salary(self, salary):
        """Set salary with validation"""
        if salary < 0:
            raise NegativeSalaryError("Salary cannot be negative")
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# Exception handling
try:
    emp1 = Employee("Raj", 25, 50000)
    emp1.display()
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except NegativeSalaryError as e:
    print(f"NegativeSalaryError: {e}")
finally:
    print("Employee creation attempt completed.\n")

# Invalid age
try:
    emp2 = Employee("Priya", 15, 60000)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
finally:
    print("Handled invalid age.\n")

# Negative salary
try:
    emp3 = Employee("Rahul", 30, -5000)
except NegativeSalaryError as e:
    print(f"NegativeSalaryError: {e}")
finally:
    print("Handled negative salary.")
