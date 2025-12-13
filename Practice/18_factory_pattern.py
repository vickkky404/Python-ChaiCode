# Factory Pattern

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat,
            'bird': Bird
        }
        
        if animal_type.lower() in animals:
            return animals[animal_type.lower()]()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Testing
factory = AnimalFactory()

animal_types = ['dog', 'cat', 'bird']
for animal_type in animal_types:
    animal = factory.create_animal(animal_type)
    print(f"{animal_type.capitalize()} says: {animal.speak()}")
