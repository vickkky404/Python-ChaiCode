# OOPS Program 16: Type Hints and Dataclasses
# Demonstrates type hints and dataclass decorator

from dataclasses import dataclass
from typing import List

@dataclass
class Person:
    name: str
    age: int
    email: str
    
    def display(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}, Email: {self.email}')

@dataclass
class Team:
    team_name: str
    members: List[Person]
    
    def add_member(self, person: Person) -> None:
        self.members.append(person)
    
    def get_team_info(self) -> str:
        return f'Team: {self.team_name}, Members: {len(self.members)}'

if __name__ == '__main__':
    p1 = Person('Raj', 25, 'raj@example.com')
    p2 = Person('Priya', 24, 'priya@example.com')
    
    p1.display()
    p2.display()
    
    team = Team('Development', [p1])
    team.add_member(p2)
    print(team.get_team_info())
