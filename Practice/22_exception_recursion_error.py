# Exception Handling - Recursion Error
# Demonstrates RecursionError with infinite recursion

def infinite_recursion(n=0):
    """Function that causes infinite recursion"""
    try:
        return infinite_recursion(n + 1)
    except RecursionError:
        print(f"Error: Maximum recursion depth exceeded at {n}")
    finally:
        print("Recursion error check completed.")

def safe_recursion(n, max_depth=5):
    """Safe recursion with depth limit"""
    if n >= max_depth:
        return n
    return safe_recursion(n + 1, max_depth)

if __name__ == "__main__":
    infinite_recursion()
