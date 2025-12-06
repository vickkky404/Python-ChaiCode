# Exception handling with string methods
try:
    text = "Hello"
    index = text.index("x")
except ValueError as e:
    print(f"Value not found: {e}")
