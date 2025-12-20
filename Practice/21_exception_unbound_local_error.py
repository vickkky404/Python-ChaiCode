# Exception Handling - Unbound Local Error
# Demonstrates UnboundLocalError

def modify_global_variable():
    """Function to demonstrate unbound local error"""
    global_var = 10
    try:
        print(f"Before: {global_var}")
        if True:
            global_var += 5
        print(f"After: {global_var}")
    except UnboundLocalError:
        print("Error: Variable referenced before assignment!")
    finally:
        print("Unbound local error check completed.")

if __name__ == "__main__":
    modify_global_variable()
