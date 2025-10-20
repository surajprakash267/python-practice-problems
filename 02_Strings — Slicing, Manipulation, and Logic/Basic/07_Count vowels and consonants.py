#.                Count vowels and consonants.

x = input("Enter the string: ").lower()
vowels = "aeiou"
count_vowel = 0
count_consonant = 0

for i in x:
    if i.isalpha():  # checks if it's a letter
        if i in vowels:
            count_vowel += 1
        else:
            count_consonant += 1

print(f"No. of vowels: {count_vowel}")
print(f"No. of consonants: {count_consonant}")
