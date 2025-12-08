# OOPS Program 27: String Representation Magic Methods
# Demonstrates __str__ and __repr__ differences

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
    def __repr__(self):
        return f'Person("{self.name}", {self.age})'

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.pages})'

if __name__ == '__main__':
    person = Person('Raj', 25)
    print('str():', str(person))
    print('repr():', repr(person))
    
    book = Book('Python Guide', 'Guido', 500)
    print('str():', str(book))
    print('repr():', repr(book))
