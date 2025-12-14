"""Command Pattern - Encapsulate a request as an object, allowing parameterization of clients."""

from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    """Abstract command interface."""
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


class Light:
    """Receiver class."""
    
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print("Light is ON")
    
    def turn_off(self):
        self.is_on = False
        print("Light is OFF")


class LightOnCommand(Command):
    """Concrete command to turn on light."""
    
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    """Concrete command to turn off light."""
    
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
    
    def undo(self):
        self.light.turn_on()


class RemoteControl:
    """Invoker that executes commands."""
    
    def __init__(self):
        self.commands: List[Command] = []
        self.history: List[Command] = []
    
    def add_command(self, command: Command):
        self.commands.append(command)
    
    def execute_commands(self):
        for command in self.commands:
            command.execute()
            self.history.append(command)
    
    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Demonstration
if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()
    
    on_command = LightOnCommand(light)
    off_command = LightOffCommand(light)
    
    remote.add_command(on_command)
    remote.add_command(off_command)
    remote.add_command(on_command)
    
    print("Executing commands:")
    remote.execute_commands()
    
    print("\nUndoing last command:")
    remote.undo()
    
    print("Undoing another command:")
    remote.undo()
