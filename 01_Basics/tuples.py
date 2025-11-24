Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tea_types = ("Black", "Green", "Oolong")
tea_types
('Black', 'Green', 'Oolong')
tea_types[0]
'Black'
tea_types[1:]
('Green', 'Oolong')
tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tea_types[0] = "Lemon"
TypeError: 'tuple' object does not support item assignment

len(tea_types)
3

more_tea = ("Herbal", "Earl Grey")
more_tea
('Herbal', 'Earl Grey')
all_tea = more_tea + tea_types
all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

if "Green" in all_tea:
    print("I have green tea")

    
I have green tea


more_tea = ("herbal", "earl grey" , "Herbal")
more_tea.count("Herbal")
1

tea_types
('Black', 'Green', 'Oolong')
(black, green, Oolong) = tea_types
black
'Black'
green
'Green'
type(tea_types)
<class 'tuple'>
("",(1,2,3),"")
('', (1, 2, 3), '')
