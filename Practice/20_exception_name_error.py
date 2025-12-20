# Exception Handling - Name Error
# Demonstrates NameError when variable is not defined

def access_undefined_variable():
    """Function to demonstrate name error handling"""
    try:
        print(f"Value of undefined_var: {undefined_var}")
    except NameError:
        print("Error: The variable has not been defined!")
    finally:
        print("Name error check completed.")

if __name__ == "__main__":
    access_undefined_variable()
