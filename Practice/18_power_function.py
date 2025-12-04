# Power Function

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:
        return 1 / power(base, -exponent)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
