# OOPS Program 5: Abstraction
# Demonstrate abstract base classes and methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def start(self):
        print("Car engine started")
    
    def stop(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")
    
    def stop(self):
        print("Bike engine stopped")

# Create objects and use them
car = Car()
car.info()
car.start()
car.stop()

bike = Bike()
bike.info()
bike.start()
bike.stop()
