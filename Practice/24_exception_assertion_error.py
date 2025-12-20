# Exception Handling - Assertion Error
# Demonstrates AssertionError with assertions

def check_age(age):
    """Function to check age with assertions"""
    try:
        assert age >= 0, "Age cannot be negative!"
        assert age <= 150, "Age seems unrealistic!"
        print(f"Age {age} is valid.")
    except AssertionError as e:
        print(f"Assertion Error: {str(e)}")
    finally:
        print("Age check completed.")

if __name__ == "__main__":
    check_age(25)
    check_age(-5)
    check_age(200)
