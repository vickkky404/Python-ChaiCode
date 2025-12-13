# Composition - HAS-A Relationship

class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        return f"Engine with {self.power}HP started"

class Wheel:
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        return f"Wheel of size {self.size} rotating"

class Car:
    def __init__(self, name, engine_power, wheel_size):
        self.name = name
        self.engine = Engine(engine_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def start_car(self):
        return self.engine.start()
    
    def drive(self):
        wheel_msg = [w.rotate() for w in self.wheels]
        return f"{self.name} is driving: {wheel_msg[0]}"

# Testing
car = Car("Tesla", 200, 18)
print(car.start_car())
print(car.drive())
print(f"Car has {len(car.wheels)} wheels")
