# Exception Handling - Overflow Error
# Demonstrates OverflowError with large numbers

import math

def check_overflow():
    """Function to check overflow error"""
    try:
        large_number = 10 ** 1000
        result = math.exp(large_number)
        print(f"Result: {result}")
    except OverflowError:
        print("Error: The result is too large to represent!")
    finally:
        print("Overflow error check completed.")

if __name__ == "__main__":
    check_overflow()
