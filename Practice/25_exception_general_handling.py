# Exception Handling - General Exception Handling
# Demonstrates comprehensive exception handling

def general_exception_demo():
    """Function to demonstrate general exception handling"""
    try:
        # Multiple potential exceptions
        numbers = [1, 2, 3]
        print(f"Number: {numbers[5]}")
        result = 10 / 0
        x = int("abc")
    except (IndexError, ZeroDivisionError, ValueError) as e:
        print(f"Error caught: {type(e).__name__} - {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    else:
        print("No exception occurred!")
    finally:
        print("Exception handling completed.")

if __name__ == "__main__":
    general_exception_demo()
