"""Visitor Pattern - Represent operation to be performed on elements without changing classes."""
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_cat(self, cat): pass
    @abstractmethod
    def visit_dog(self, dog): pass

class Animal(ABC):
    @abstractmethod
    def accept(self, visitor): pass

class Cat(Animal):
    def accept(self, visitor):
        return visitor.visit_cat(self)
    def meow(self):
        return 'Meow!'

class Dog(Animal):
    def accept(self, visitor):
        return visitor.visit_dog(self)
    def bark(self):
        return 'Woof!'

class SoundVisitor(Visitor):
    def visit_cat(self, cat):
        return f'Cat says: {cat.meow()}'
    def visit_dog(self, dog):
        return f'Dog says: {dog.bark()}'

class DescriptionVisitor(Visitor):
    def visit_cat(self, cat):
        return 'This is a cute cat'
    def visit_dog(self, dog):
        return 'This is a loyal dog'

if __name__ == '__main__':
    animals = [Cat(), Dog()]
    sound_visitor = SoundVisitor()
    desc_visitor = DescriptionVisitor()
    for animal in animals:
        print(animal.accept(sound_visitor))
        print(animal.accept(desc_visitor))
