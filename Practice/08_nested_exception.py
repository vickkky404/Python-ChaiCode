# Nested try-except blocks

try:
    outer_var = 10
    try:
        inner_var = 0
        result = outer_var / inner_var
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero!")
        inner_var = 5
        result = outer_var / inner_var
    print(f"Result: {result}")
except Exception as e:
    print(f"Outer Exception: {e}")
