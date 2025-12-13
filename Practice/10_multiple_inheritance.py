# Multiple Inheritance

class Animal:
    def speak(self):
        return "Some sound"

class Pet:
    def cuddle(self):
        return "Cuddles provided"

class Dog(Animal, Pet):
    def speak(self):
        return "Woof!"
    
    def fetch(self):
        return "Fetches the ball"

class Cat(Animal, Pet):
    def speak(self):
        return "Meow!"
    
    def scratch(self):
        return "Scratches the furniture"

# Testing
dog = Dog()
print(f"Dog speaks: {dog.speak()}")
print(f"Dog action: {dog.fetch()}")
print(f"Dog cuddles: {dog.cuddle()}")

cat = Cat()
print(f"\nCat speaks: {cat.speak()}")
print(f"Cat action: {cat.scratch()}")
print(f"Cat cuddles: {cat.cuddle()}")

print(f"\nMRO: {Dog.__mro__}")
