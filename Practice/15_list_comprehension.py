# Program 15: List Comprehension
print("List Comprehension Examples:")

# Squares of numbers 1-5
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Even numbers from 1-10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Uppercase strings
words = ["python", "java", "javascript"]
upperwords = [word.upper() for word in words]
print(f"Uppercase: {upperwords}")

# Nested comprehension - pairs
pairs = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print(f"Pairs: {pairs}")

# Filtering and transformation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x*2 for x in numbers if x > 5]
print(f"Double numbers >5: {result}")
