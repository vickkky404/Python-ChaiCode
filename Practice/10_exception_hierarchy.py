# Exception hierarchy - catching parent catches child exceptions
try:
    x = [1, 2, 3]
    print(x[10])
except IndexError as e:
    print(f"IndexError: {e}")
except Exception:
    print("Generic exception caught")
