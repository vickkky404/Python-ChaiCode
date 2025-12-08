# OOPS Program 18: Descriptors
# Demonstrates descriptor protocol (__get__, __set__, __delete__)

class PositiveInt:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f'{self.name} must be positive')
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]

class Person:
    age = PositiveInt('age')
    salary = PositiveInt('salary')
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}')

if __name__ == '__main__':
    p = Person('Raj', 25, 60000)
    p.display()
    p.age = 26
    p.salary = 70000
    p.display()
