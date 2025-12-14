"""State Pattern - Allow an object to alter its behavior when its internal state changes."""

from abc import ABC, abstractmethod


class State(ABC):
    """Abstract state interface."""
    
    @abstractmethod
    def handle(self, context: 'TrafficLight'):
        pass


class RedLight(State):
    """Concrete state for red light."""
    
    def handle(self, context: 'TrafficLight'):
        print("Red Light - STOP")
        context.state = GreenLight()


class GreenLight(State):
    """Concrete state for green light."""
    
    def handle(self, context: 'TrafficLight'):
        print("Green Light - GO")
        context.state = YellowLight()


class YellowLight(State):
    """Concrete state for yellow light."""
    
    def handle(self, context: 'TrafficLight'):
        print("Yellow Light - PREPARE TO STOP")
        context.state = RedLight()


class TrafficLight:
    """Context that uses state."""
    
    def __init__(self):
        self.state = RedLight()
    
    def change_light(self):
        """Change the light state."""
        self.state.handle(self)


# Demonstration
if __name__ == "__main__":
    light = TrafficLight()
    
    for _ in range(6):
        light.change_light()
