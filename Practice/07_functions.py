# Program 7: Functions
def greet():
    print("Hello, Welcome!")

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

greet()
result1 = add(10, 20)
print(f"10 + 20 = {result1}")

result2 = multiply(5, 4)
print(f"5 x 4 = {result2}")

def greet_person(name):
    return f"Hello, {name}!"

print(greet_person("Vikram"))
