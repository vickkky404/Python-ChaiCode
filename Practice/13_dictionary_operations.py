# Exception with dictionary operations
try:
    d = {"a": 1, "b": 2}
    value = d["c"]
except KeyError:
    print("Key not found!")
