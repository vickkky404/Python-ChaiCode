n = int(input("Enter a number: "))
num = n
digit_sum = sum(int(d) ** len(str(n)) for d in str(abs(n)))
print(f"{n} is Armstrong" if digit_sum == num else f"{n} is not Armstrong")
