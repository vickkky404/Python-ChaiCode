# Digit Sum

def digit_sum(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
result = digit_sum(num)
print(f"Sum of digits of {num} is {result}")
