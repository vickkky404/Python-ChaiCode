# OOPS Program 21: Slots for Memory Optimization
# Demonstrates __slots__ to optimize memory usage

class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class WithSlots:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ComplexClass:
    __slots__ = ('_name', '_email', '_phone', '_address')
    
    def __init__(self, name, email, phone, address):
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
    
    def get_info(self):
        return f'{self._name} - {self._email} - {self._phone}'

if __name__ == '__main__':
    obj1 = WithoutSlots('Raj', 25)
    obj2 = WithSlots('Priya', 24)
    
    print('Without slots dict:', obj1.__dict__)
    print('With slots (no dict):', 'No __dict__ attribute')
    
    complex_obj = ComplexClass('Arjun', 'arjun@example.com', '9876543210', 'Bangalore')
    print(complex_obj.get_info())
