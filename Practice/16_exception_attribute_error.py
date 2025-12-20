# Exception Handling - Attribute Error
# Demonstrates AttributeError when accessing non-existent attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def access_attribute():
    """Function to access object attributes with exception handling"""
    try:
        person = Person("Alice", 30)
        attribute = input("Enter the attribute to access: ")
        value = getattr(person, attribute)
        print(f"{attribute}: {value}")
    except AttributeError:
        print(f"Error: Attribute not found in the object!")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        print("Attribute access operation completed.")

if __name__ == "__main__":
    access_attribute()
