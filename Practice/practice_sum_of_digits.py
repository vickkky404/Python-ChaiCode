n = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(n)))
print(f"Sum of digits: {digit_sum}")
