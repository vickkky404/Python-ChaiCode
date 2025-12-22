# Program 10: Dictionary Operations
student = {"name": "Vikram", "age": 25, "city": "Odisha", "cgpa": 8.5}
print(f"Dictionary: {student}")
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")

print(f"\nAccessing values:")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

student["college"] = "CUTM"
print(f"\nAfter adding college: {student}")

del student["cgpa"]
print(f"After deleting cgpa: {student}")

print(f"\nIterating:")
for key, value in student.items():
    print(f"  {key}: {value}")
