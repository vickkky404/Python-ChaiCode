10_simple_calculator.py# Simple Calculator
# Perform basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == '+':
    print(f"Result: {add(num1, num2)}")
elif operation == '-':
    print(f"Result: {subtract(num1, num2)}")
elif operation == '*':
    print(f"Result: {multiply(num1, num2)}")
elif operation == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation")
