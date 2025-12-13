# Data Classes
from dataclasses import dataclass, field
from typing import List

@dataclass
class Address:
    street: str
    city: str
    zip_code: str
    
    def __str__(self):
        return f"{self.street}, {self.city} {self.zip_code}"

@dataclass
class Person:
    name: str
    age: int
    email: str
    address: Address
    hobbies: List[str] = field(default_factory=list)
    
    def is_adult(self):
        return self.age >= 18
    
    def __str__(self):
        return f"{self.name} ({self.age}) - {self.email}"

# Testing
address = Address("123 Main St", "New York", "10001")
person = Person(
    name="Alice",
    age=25,
    email="alice@example.com",
    address=address,
    hobbies=["coding", "reading"]
)

print(person)
print(f"Address: {person.address}")
print(f"Hobbies: {person.hobbies}")
print(f"Is adult: {person.is_adult()}")

person2 = Person("Bob", 30, "bob@example.com", address)
print(f"\nperson == person2: {person == person2}")
