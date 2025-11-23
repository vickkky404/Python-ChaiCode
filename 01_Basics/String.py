Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
chai = "Lemon Chai"
chai
'Lemon Chai'
print(chai)
Lemon Chai
chai1 = "Masala Chai"
first_char =  chai[0]_
SyntaxError: invalid syntax
first_char =  chai[0]
print(chai)
Lemon Chai


cha
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cha
NameError: name 'cha' is not defined. Did you mean: 'chai'?
chai
'Lemon Chai'
slice_chai = chai[0:5]
print(slice_chai)
Lemon
chai[0:6]
'Lemon '
chai[-1]
'i'
num_list = "0123456789"
num_list[:]
'0123456789'
num_list[:]
'0123456789'
num_list[0:7:2]
'0246'
chau
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    chau
NameError: name 'chau' is not defined. Did you mean: 'chai'?
chai
'Lemon Chai'
print(chai.lower())
lemon chai
print(chai.upper())
LEMON CHAI
chai = "   Masala Chai   "
chai
'   Masala Chai   '
print(chai.strip())
Masala Chai
chai = "lemon chai"
print(chai.replace("Lemon" , "Ginger"))
lemon chai
chai
'lemon chai'
print(chai.replace("lemon", "Ginger"))
Ginger chai
chai
'lemon chai'
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
chai = "Masala chai"
print(chai.find("Chai))
                
SyntaxError: unterminated string literal (detected at line 1)
print(chai.find("Chai"))
                
-1
chai = "Masala Chai Chai Chai"
                
print(chai.count("Chai"))
                
3


chai_type = "Masala"
                
quantity = 2
                
order = "I ordered {} cups of {} chai"
                
order
                
'I ordered {} cups of {} chai'
print(order.format(quantity, chai, chai_type))
                
I ordered 2 cups of Masala Chai Chai Chai chai


chai_variety = ["Lemon", "Masala", "Ginger"]
                
chai_variety
                
['Lemon', 'Masala', 'Ginger']
print("".join()chai_variety)
                
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(" ".join(chai_variety))
                
Lemon Masala Ginger
chai = "Masala Chai"
                
chai
                
'Masala Chai'
print(len(chai))
                
11
