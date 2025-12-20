# Exception Handling - Value Error
# Demonstrates ValueError when type conversion fails

def convert_to_int():
    """Function to convert string to integer with exception handling"""
    try:
        value = input("Enter a value to convert to integer: ")
        result = int(value)
        print(f"Converted value: {result}")
    except ValueError:
        print(f"Error: '{value}' cannot be converted to an integer!")
    finally:
        print("Conversion operation completed.")

if __name__ == "__main__":
    convert_to_int()
