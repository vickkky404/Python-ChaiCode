# Program 3: User Input
# Demonstrates taking input from user and displaying output

print("=== User Input Program ===")
print()

# Taking string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Taking integer input
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Taking float input
height = float(input("Enter your height (in feet): "))
print(f"Your height is {height} feet")

# Multiple inputs on same line
print()
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

sum_result = first_num + second_num
print(f"\nSum of {first_num} and {second_num} is {sum_result}")
