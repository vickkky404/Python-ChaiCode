# Exception Handling - Type Error
# Demonstrates TypeError when wrong type is passed

def add_numbers():
    """Function to add numbers with exception handling"""
    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        # Attempting to add strings instead of numbers
        result = num1 + num2
        print(f"Sum: {result}")
    except TypeError:
        print("Error: Cannot perform operation with incompatible types!")
    finally:
        print("Addition operation completed.")

if __name__ == "__main__":
    add_numbers()
