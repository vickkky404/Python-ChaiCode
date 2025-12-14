"""Composite Pattern - Compose objects into tree structures."""
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self): pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name
    
    def operation(self):
        return f'Leaf({self.name})'

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        result = [f'Composite({self.name})']
        for child in self.children:
            result.append(child.operation())
        return ' '.join(result)

if __name__ == '__main__':
    root = Composite('root')
    root.add(Leaf('A'))
    branch = Composite('branch')
    branch.add(Leaf('B'))
    branch.add(Leaf('C'))
    root.add(branch)
    print(root.operation())
