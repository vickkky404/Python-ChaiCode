# Exception Handling - Division by Zero
# Demonstrates how to handle ZeroDivisionError exception

def divide_numbers():
    """Function to divide two numbers with exception handling"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    finally:
        print("Division operation completed.")

if __name__ == "__main__":
    divide_numbers()
