# Vowel Counter

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print(f"Number of vowels: {vowel_count}")
