# Raise exceptions explicitly

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot exceed 150!")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    return f"Valid age: {age}"

try:
    print(validate_age(25))
    print(validate_age(-5))
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
