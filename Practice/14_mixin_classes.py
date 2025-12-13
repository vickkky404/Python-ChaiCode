# Mixin Classes

class Serializable:
    def to_dict(self):
        return self.__dict__
    
    def to_json(self):
        import json
        return json.dumps(self.to_dict())

class Comparable:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __lt__(self, other):
        return len(self.__dict__) < len(other.__dict__)

class Person(Serializable, Comparable):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age}"

# Testing
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(f"p1: {p1}")
print(f"p1 as dict: {p1.to_dict()}")
print(f"p1 as JSON: {p1.to_json()}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p2: {p1 < p2}")
