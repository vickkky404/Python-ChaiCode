# Program 9: String Operations
text = "Python Programming"
print(f"Original: {text}")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

print(f"\nSlicing:")
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[7:]}")
print(f"Reversed: {text[::-1]}")

print(f"\nString methods:")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

name = "Vikram"
age = 25
print(f"\nFormatting: {name} is {age} years old")
