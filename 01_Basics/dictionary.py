 # order doesnot matter in dictionary , and doesnot matters in list

chai_types = {"Masala":"Spicy" , "Ginger":"Zesty" , "Green":"Mild"}
print(chai_types)

# accessing
print(chai_types["Masala"])

# updating
chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai)
