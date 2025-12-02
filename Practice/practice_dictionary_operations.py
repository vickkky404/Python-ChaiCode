d = {"name": "Alice", "age": 25, "city": "Mumbai"}
d["email"] = "alice@example.com"
print(f"Keys: {d.keys()}")
print(f"Values: {d.values()}")
print(f"Items: {d.items()}")
if "age" in d:
    print(f"Age: {d.get('age')}")
d.update({"country": "India"})
print(d)
