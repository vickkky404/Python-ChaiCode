# Palindrome String Checker
# Check if a string reads same forwards and backwards

string = input("Enter a string: ").lower().replace(" ", "")
reversed_string = string[::-1]

if string == reversed_string:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
