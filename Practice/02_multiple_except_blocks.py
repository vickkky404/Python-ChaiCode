# Multiple except blocks for different exception types

try:
    file = open('nonexistent.txt', 'r')
    data = file.read()
    number = int(data)
except FileNotFoundError:
    print("Error: File not found!")
except ValueError:
    print("Error: Could not convert to integer!")
except IOError:
    print("Error: IO operation failed!")
finally:
    print("Execution completed.")
