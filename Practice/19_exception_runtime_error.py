# Exception Handling - Runtime Error
# Demonstrates RuntimeError for runtime issues

def check_runtime_error():
    """Function to demonstrate runtime error handling"""
    try:
        x = 5
        y = 0
        if y == 0:
            raise RuntimeError("Cannot perform operation with y=0")
        result = x / y
        print(f"Result: {result}")
    except RuntimeError as e:
        print(f"Runtime Error: {str(e)}")
    finally:
        print("Runtime check completed.")

if __name__ == "__main__":
    check_runtime_error()
