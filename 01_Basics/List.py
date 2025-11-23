from gevent.greenlet import Greenlet

tea_varities =["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[-1])
print(tea_varities[1:3])

print(tea_varities[:2])

tea_varities[3] = "herbal"

print(tea_varities)

tea_varities[1:3]

tea_varities[3] = "White"
print(tea_varities)

# replacing 2 lists in once
tea_varities[1:3]= ["green" , "Masala"]
print(tea_varities)

# clean coding..
tea_varities[1:1] = ["test", "test"]
print(tea_varities)

tea_varities[1:3] = []
print(tea_varities)

for tea in tea_varities:
    print(tea)


for tea in tea_varities:
    print(tea, end="-")


if "Oolang" in tea_varities:
    print("I have Oolang")
else:
    print("i dont have Oolang tea")



tea_varities.pop()
print(tea_varities)

# remove
tea_varities.remove("green")
print(tea_varities)

# add
tea_varities.insert(1, "Green")
print(tea_varities)


# a copy with a diffrent referance..
tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

tea_varities_copy.append("Lemon")
print(tea_varities_copy)