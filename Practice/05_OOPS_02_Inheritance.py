# OOPS Program 2: Inheritance
# Demonstrate inheritance between parent and child classes

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
    def describe(self):
        print(f"This is {self.name}")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Create instances and demonstrate inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.describe()
dog.speak()

cat.describe()
cat.speak()
