# Fibonacci Sequence Generator
# Generate fibonacci sequence up to n terms

terms = int(input("How many fibonacci terms to generate? "))
fib_sequence = []

if terms <= 0:
    print("Please enter a positive number")
elif terms == 1:
    fib_sequence = [0]
else:
    a, b = 0, 1
    for _ in range(terms):
        fib_sequence.append(a)
        a, b = b, a + b

print(f"Fibonacci sequence: {fib_sequence}")
