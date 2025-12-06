# Basic try-except block
# Demonstrates basic exception handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
