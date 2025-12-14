"""Advanced Decorator Pattern - Add responsibilities dynamically."""
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self): pass
    @abstractmethod
    def description(self): pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 1.0
    def description(self):
        return 'Simple Coffee'

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

class Milk(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.5
    def description(self):
        return self.coffee.description() + ', Milk'

class Sugar(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.2
    def description(self):
        return self.coffee.description() + ', Sugar'

class Chocolate(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.7
    def description(self):
        return self.coffee.description() + ', Chocolate'

if __name__ == '__main__':
    coffee = SimpleCoffee()
    coffee = Milk(coffee)
    coffee = Sugar(coffee)
    coffee = Chocolate(coffee)
    print(f'{coffee.description()}: ${coffee.cost():.2f}')
