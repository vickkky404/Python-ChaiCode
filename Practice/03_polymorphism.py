# OOPS - Polymorphism
# Demonstrates method overriding and polymorphism in Python

class Bird:
    """Base class for birds"""
    
    def speak(self):
        print("Bird speaks")
    
    def fly(self):
        print("Bird is flying")

class Parrot(Bird):
    """Derived class overriding parent methods"""
    
    def speak(self):
        print("Parrot says: Hello!")

class Sparrow(Bird):
    """Another derived class with different implementation"""
    
    def speak(self):
        print("Sparrow chirps: Chirp chirp!")

class Eagle(Bird):
    """Third derived class"""
    
    def speak(self):
        print("Eagle screams")

# Polymorphism in action
birds = [Parrot(), Sparrow(), Eagle()]
for bird in birds:
    bird.speak()
    bird.fly()
