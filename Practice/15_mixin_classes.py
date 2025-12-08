# OOPS Program 15: Mixin Classes
# Demonstrates multiple inheritance using Mixin classes

class Swimmer:
    def swim(self):
        print('Swimming...')

class Flyer:
    def fly(self):
        print('Flying...')

class Runner:
    def run(self):
        print('Running...')

class Duck(Swimmer, Flyer):
    def quack(self):
        print('Quack Quack!')

class Penguin(Swimmer, Runner):
    def waddle(self):
        print('Waddling...')

class Pigeon(Flyer, Runner):
    def coo(self):
        print('Coo Coo!')

if __name__ == '__main__':
    duck = Duck()
    duck.swim()
    duck.fly()
    duck.quack()
    
    penguin = Penguin()
    penguin.swim()
    penguin.run()
    penguin.waddle()
    
    pigeon = Pigeon()
    pigeon.fly()
    pigeon.run()
    pigeon.coo()
