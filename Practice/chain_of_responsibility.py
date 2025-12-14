"""Chain of Responsibility - Pass request along chain of handlers."""
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request): pass

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request <= 10:
            print(f'Handler 1 handled {request}')
        elif self.next_handler:
            self.next_handler.handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if 10 < request <= 20:
            print(f'Handler 2 handled {request}')
        elif self.next_handler:
            self.next_handler.handle(request)

class ConcreteHandler3(Handler):
    def handle(self, request):
        if request > 20:
            print(f'Handler 3 handled {request}')

if __name__ == '__main__':
    h1, h2, h3 = ConcreteHandler1(), ConcreteHandler2(), ConcreteHandler3()
    h1.set_next(h2).set_next(h3)
    for val in [5, 15, 25]:
        h1.handle(val)
