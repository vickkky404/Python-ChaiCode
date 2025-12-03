# String Reversal Program
# Reverse a string using different methods

string = input("Enter a string: ")

# Method 1: Using slicing
reversed_string = string[::-1]

print(f"Original string: {string}")
print(f"Reversed string: {reversed_string}")

# Method 2: Using loop
reversed_loop = ""
for char in string:
    reversed_loop = char + reversed_loop

print(f"Reversed using loop: {reversed_loop}")
