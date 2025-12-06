# Assert statement for debugging

def check_positive(num):
    assert num > 0, "Number must be positive!"
    assert isinstance(num, (int, float)), "Must be a number!"
    return num * 2

try:
    result = check_positive(5)
    print(f"Result: {result}")
    bad_result = check_positive(-10)
except AssertionError as e:
    print(f"Assertion Error: {e}")
